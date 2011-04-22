import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from datetime import datetime
from censo.models import *
import sys
import psycopg2
import re
from datetime import *
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db import transaction

months = (
    ('enero', 1),
    ('febrero', 2),
    ('marzo', 3),
    ('abril', 4),
    ('mayo', 5),
    ('junio', 6),
    ('julio', 7),
    ('agosto', 8),
    ('septiembre', 9),
    ('octubre', 10),
    ('noviembre', 11),
    ('diciembre', 12),
)

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

def main():
    conn_string = "host='127.0.0.1' dbname='mydb' port='5432' user='cc61a' password='cc61a'"
    
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    print 'Deleting UserHasRole'
    UserHasRole.objects.all().delete()
    
    print 'Deleting UserProfile'
    UserProfile.objects.all().delete()
    print 'Deleting Role'
    Role.objects.all().delete()
    print 'Deleting Users'
    User.objects.filter(is_superuser = False).delete()
    
    Cuerpo.objects.all().delete()
    Region.objects.all().delete()
    Province.objects.all().delete()
    Commune.objects.all().delete()
    Company.objects.all().delete()


    #print 'Migrando regiones'
    cursor.execute("SELECT * FROM regiones")
    rows = cursor.fetchall()
    for row in rows:
        num_region = row[0]
        name_region = row[1]
        
        region = Region()
        region.number = num_region
        region.name = name_region
        #print region
        region.save()
        
    #print 'Migrando provincias'
    cursor.execute("SELECT * FROM provincias")
    rows = cursor.fetchall()
    for row in rows:
        province = Province()
        old_id = row[0]
        name = row[1]
        region_number = row[2]
        region = Region.objects.get(number = row[2])
        province.name = name
        province.region = region
        province.old_id = old_id
        #print province
        province.save()
        
    #print 'Migrando comunas'
    cursor.execute("SELECT * FROM comuna")
    rows = cursor.fetchall()
    for row in rows:
        prov_id = row[4]
        province = Province.objects.get(old_id = prov_id)
        commune = Commune()
        commune.name = row[1]
        url = row[3]
        if not url:
            url = ''
        commune.url = url
        commune.province = province
        #print commune
        commune.save()
        
    #print 'Migrando cuerpos'
    cursor.execute("SELECT * FROM cuerpos")
    rows = cursor.fetchall()
    
    pending_cuerpos_communes = []
    pending_cuerpos_attend_communes = []
    pending_cuerpos_foundation_dates = []
    pending_cuerpos_decree_dates = []
    pending_cuerpos_cuer_nper_juris = []
    
    for row in rows:
        cuerpo = Cuerpo()
        cuerpo.old_id = row[0]
        cuerpo.name = row[1]
        cuerpo.rut = row[2].replace('.', '').replace('-', '').lower()
        cuerpo.address = row[4]
        commune_name = row[5]
        
        try:
            commune = Commune.objects.get(name__iexact = commune_name)
            cuerpo.commune = commune
        except Commune.DoesNotExist:
            pending_cuerpos_communes.append([cuerpo, commune_name])
            
        cuerpo.save()
        
        commune_names = row[14]
        if commune_names:
            communes = [commune.strip() for commune in commune_names.split(',')]
            for commune_name in communes:
                try:
                    commune = Commune.objects.get(name__iexact = commune_name)
                    cuerpo.communes.add(commune)
                except:
                    pending_cuerpos_attend_communes.append([cuerpo, commune_name])
                
        cuerpo.save()
        
        cuerpo.phone = row[6]
        cuerpo.fax = row[7]
        postal_box = row[8]
        if postal_box:
            cuerpo.postal_box = postal_box
        mail = row[9]
        if mail:
            cuerpo.mail = mail
        url = row[10]
        if url:
            cuerpo.url = url
        cuerpo.save()
        
        # fecha fundacion

        date_string = row[11]

        if date_string:
            date_string = date_string.lower()
            
            for month_name, value in months:
                date_string = date_string.replace(month_name, str(value))
            
            m = re.search('(\d+)\D+(\d+)\D+(\d+)', date_string)
            if m:
                day = int(m.group(1))
                if day > 31:
                    raise Exception
                month = int(m.group(2))
                year = int(m.group(3))
                d = date(year, month, day)
                cuerpo.foundation_date = d
            else:
                pending_cuerpos_foundation_dates.append([cuerpo, date_string])
        
        lemma = row[12]
        
        if lemma:
            # http://stackoverflow.com/questions/2872512/python-truncate-a-long-string
            cuerpo.lemma = lemma[:252] + (lemma[252:] and '...')
            # cuerpo.lemma = lemma
            cuerpo.save()

        alarm_central_phone = row[13]
        if alarm_central_phone:
            cuerpo.alarm_central_phone = alarm_central_phone
            
        cuer_npers_juri = row[16]
        if cuer_npers_juri:
            try:
                cuer_npers_juri_num = int(cuer_npers_juri)
                cuerpo.cuer_npers_juri = cuer_npers_juri_num
            except ValueError, e:
                pending_cuerpos_cuer_nper_juris.append([cuerpo, cuer_npers_juri])

        date_string = row[17]

        if date_string:
            date_string = date_string.lower()
            
            for month_name, value in months:
                date_string = date_string.replace(month_name, str(value))
            
            m = re.search('(\d+)\D+(\d+)\D+(\d+)', date_string)
            if m:
                day = int(m.group(1))
                if day > 31:
                    raise Exception
                month = int(m.group(2))
                year = int(m.group(3))
                d = date(year, month, day)
            else:
                pending_cuerpos_decree_dates.append([cuerpo, date_string])
        
            cuerpo.decree_date = d
            
        #print cuerpo
        cuerpo.save()
        
    #print 'Migrando Companias'
    pending_companies_communes = []
    pending_companies_attend_communes = []
    pending_companies_foundation_dates = []
    
    cursor.execute('SELECT * FROM companias')
    rows = cursor.fetchall()
    for row in rows:
        company = Company()
        company.old_id = row[0]
        company.number = int(row[1])
        
        company.name = row[2]
        
        cuerpo_id = row[3]
        cuerpo = Cuerpo.objects.get(old_id = cuerpo_id)
        company.cuerpo = cuerpo
        
        phone = row[5]
        if phone:
            company.phone = phone
        mail = row[6]
        if mail:
            company.mail = mail
        address = row[8]
        if address:
            company.address = address
        
        commune_name = row[9]
        
        try:
            commune = Commune.objects.get(name__iexact = commune_name)
            company.commune = commune
        except Commune.DoesNotExist:
            pending_companies_communes.append([company, commune_name])
        except ValueError:
            pending_companies_communes.append([company, commune_name])
        
        fax = row[10]
        if fax:
            company.fax = fax
        postal_box = row[11]
        if postal_box:
            company.postal_box = postal_box
        website = row[12]
        if website:
            company.website = website
        alarm_central = row[13]
        if alarm_central:
            company.alarm_central = alarm_central
        lemma = row[14]
        if lemma:
            company.lemma = lemma
        
        company.save()
        
        commune_names = row[16]
        if commune_names:
            communes = [commune.strip() for commune in commune_names.split(',')]
            for commune_name in communes:
                try:
                    commune = Commune.objects.get(name__iexact = commune_name)
                    company.communes.add(commune)
                except:
                    pending_companies_attend_communes.append([company, commune_name])
        
        # fecha fundacion

        date_string = row[17]

        if date_string:
            date_string = date_string.lower()
            
            for month_name, value in months:
                date_string = date_string.replace(month_name, str(value))
            
            m = re.search('(\d+)\D+(\d+)\D+(\d+)', date_string)
            try:
                if m:
                    day = int(m.group(1))
                    month = int(m.group(2))
                    year = int(m.group(3))
                    if day > 31 or month > 12:
                        raise Exception
                    d = date(year, month, day)
                    company.foundation_date = d
                else:
                    pending_companies_foundation_dates.append([company, date_string])
            except:
                pending_companies_foundation_dates.append([company, date_string])
                
        #print company
        company.save()
    
            
    #print 'Migrando Roles'
    cursor.execute("SELECT * FROM cargo")
    rows = cursor.fetchall()
    for row in rows:
        name = row[1]
        if name:
            role = Role()
            role.name = name
            sid = row[0]
            if not Role.objects.filter(old_id = sid):
                role.old_id = sid
                role.save()
                #print role
                
    #print 'Migrando Usuarios'
    
    # Primero, encontrar usernames y passwords en la tabla mailbox
    print 'Fetching passwords'
    cursor.execute("SELECT * FROM mailbox")
    rows = cursor.fetchall()
    usu_dict = {}
    usernames = []
    for row in rows:
        username = row[0].split('@')[0]
        password = row[1]
        id_usu = row[12]
        if username not in usernames:
            usu_dict[id_usu] = [username, password]     
            usernames.append(username)
    
    # Segundo, migrar sus datos
    print 'Creating users'
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    pending_user_roles = []
    pending_user_companies = []
    len_rows = len(rows)
    
    transaction.enter_transaction_management()
    transaction.managed(True)
    for idx, row in enumerate(rows):
        if idx % 1000 == 0:
            print str(idx) + ' de ' + str(len_rows)
            transaction.commit()
        u = User()
        u.save()
        profile = u.get_profile()
        profile.old_id = row[0]
        profile.first_name = row[1]
        profile.first_last_name = row[2]
        profile.second_last_name = row[3]
        rut = row[4]
        if rut:
            rut = rut.replace('.', '').replace(':', '')
            try:
                profile.rut = str(int(rut))[:9]
            except ValueError:
                profile.rut = ''
        u.username = str(u.id)
        u.save()
        
        address = row[7]
        if address:
            profile.address = address

        phone = row[8]
        if phone:
            profile.phone = phone
            
        cellphone = row[9]
        if cellphone:
            profile.cell_phone = cellphone
            
        on = row[11]
        if on:
            occupation_name = on[:252] + (on[252:] and '...')
            profile.occupation, created = Occupation.objects.get_or_create(name = occupation_name)
            
        work_phone = row[12]
        if work_phone:
            profile.work_phone = work_phone
            
        work_address = row[13]
        if work_address:
            profile.work_address = work_address

        company_id = row[14]
        if company_id:
            try:
                profile.company = Company.objects.get(old_id = company_id)
            except Company.DoesNotExist:
                pending_user_companies.append([u, company_id])
                
        try:
            profile.current_role = Role.objects.get(old_id = row[16])
        except Role.DoesNotExist:
            pending_user_roles.append([u, row[16]])
        gender = row[19]
        if gender:
            profile.gender = row[19][0]
        else:
            profile.gender = 'M'
        #print profile
        profile.save()
        u.save()
        
        if profile.old_id not in usu_dict:
            continue
        username, password = usu_dict[profile.old_id]
        u.username = username
        u.set_password(password)
        u.save() 

    transaction.commit()
    transaction.leave_transaction_management()

    #transaction.enter_transaction_management()
    #transaction.managed(True)
    #print 'Migrando Roles de Usuario'
    uhr_missing_data = []
    cursor.execute("SELECT * FROM usu_cargo")
    rows = cursor.fetchall()
    
    profiles = UserProfile.objects.order_by('old_id')
    profile_ids = [p.old_id for p in profiles]
    
    roles = Role.objects.order_by('old_id')
    role_ids = [p.old_id for p in roles]
    
    cuerpos = Cuerpo.objects.order_by('old_id')
    cuerpo_ids = [p.old_id for p in cuerpos]
    
    counter = 0
    
    len_rows = len(rows)
    for idx, row in enumerate(rows):
        if idx % 100 == 0:
            print str(idx) + ' de ' + str(len_rows)
            #transaction.commit()
        if counter % 10 == 0:
            print 'Coounter=' + str(counter)
        uhr = UserHasRole()
        
        try:
            old_id = int(row[2])
            fidx = binary_search(profile_ids, old_id)
            if fidx == -1:
                counter += 1
                continue
            else:
                uhr.profile = profiles[fidx]
                
        except TypeError, e:
            counter += 1
            continue
            
        try:
            old_id = int(row[1])
            fidx = binary_search(role_ids, old_id)
            if fidx == -1:
                counter += 1
                continue
            else:
                uhr.role = roles[fidx]
                
        except TypeError, e:
            counter += 1
            continue
            
        try:
            old_id = int(row[4])
            fidx = binary_search(cuerpo_ids, old_id)
            if fidx == -1:
                counter += 1
                continue
            else:
                uhr.cuerpo = cuerpos[fidx]
                
        except TypeError, e:
            counter += 1
            continue
            
        uhr.start_date = row[5]
        uhr.end_date = row[6]
        uhr.save()
            
    #transaction.commit()
    #transaction.leave_transaction_management()
   
    
    print 'Informes de error de migracion'
    
    print '1. Cuerpos con comunas invalidas'
    for cuerpo, commune_name in pending_cuerpos_communes:
        print str(cuerpo.id) + ' ' + unicode(cuerpo) + ': ' + commune_name

    print '2. Cuerpos con comunas atendidas invalidas'
    for cuerpo, commune_name in pending_cuerpos_attend_communes:
        print str(cuerpo.id) + ' ' + unicode(cuerpo) + ': ' + commune_name  
              
    print '3. Cuerpos con fechas de fundacion invalidas'
    for cuerpo, date_string in pending_cuerpos_foundation_dates:
        print str(cuerpo.id) + ' ' + unicode(cuerpo) + ': ' + date_string

    print '4. Cuerpos con fechas de decreto invalidas'
    for cuerpo, date_string in pending_cuerpos_decree_dates:
        print str(cuerpo.id) + ' ' + unicode(cuerpo) + ': ' + date_string

    print '5. Cuerpos con nper_juris invalido'
    for cuerpo, cuer_nper_juris in pending_cuerpos_cuer_nper_juris:
        print str(cuerpo.id) + ' ' + unicode(cuerpo) + ': ' + cuer_nper_juris

    print '6. Companias con comunas invalidas'
    for company, commune_name in pending_companies_communes:
        print str(company.id) + ' ' + unicode(company) + ': ' + commune_name

    print '7. Companias con comunas atendidas invalidas'
    for company, commune_name in pending_companies_attend_communes:
        print str(company.id) + ' ' + unicode(company) + ': ' + commune_name
        
    print '8. Companias con fechas de fundacion invalidas'
    for company, date_string in pending_companies_foundation_dates:
        print str(company.id) + ' ' + unicode(company) + ': ' + date_string

    print '9. Usuarios con roles invalidos'
    for user, rolename in pending_user_roles:
        print 'Usuario ' + str(user.id) + ' Perfil ' + str(user.get_profile().id) + ': ' + rolename
        
    print '10. Usuarios con compania invalida'
    for user, rolename in pending_user_companies:
        print 'Usuario ' + str(user.id) + ' Perfil ' + str(user.get_profile().id) + ': ' + rolename
        
    print '11. Errores en UHR'
    for error in uhr_missing_data:
        print error
    
if __name__ == '__main__':
    print datetime.now()
    main()
