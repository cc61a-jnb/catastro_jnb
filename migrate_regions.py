import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from datetime import datetime
from censo.models import *
import sys
import psycopg2
import re
from datetime import *

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

def main():
    conn_string = "host='127.0.0.1' dbname='mydb' port='5432' user='cc61a' password='cc61a'"
    
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM regiones")
    
    Role.objects.all().delete()
    Cuerpo.objects.all().delete()
    Region.objects.all().delete()
    Province.objects.all().delete()
    Commune.objects.all().delete()

    print 'Migrando regiones'
    rows = cursor.fetchall()
    for row in rows:
        num_region = row[0]
        name_region = row[1]
        
        region = Region()
        region.number = num_region
        region.name = name_region
        print region
        region.save()
        
    print 'Migrando provincias'
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
        print province
        province.save()
        
    print 'Migrando comunas'
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
        print commune
        commune.save()
        
    print 'Migrando cuerpos'
    cursor.execute("SELECT * FROM cuerpos")
    rows = cursor.fetchall()
    
    pending_cuerpos_communes = []
    pending_cuerpos_attend_communes = []
    
    for row in rows:
        cuerpo = Cuerpo()
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
        cuerpo.mail = row[9]
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
                month = int(m.group(2))
                year = int(m.group(3))
                d = date(year, month, day)
                print date_string.encode('ascii', 'ignore')
                print d
            else:
                print 'No parseable, {0}'.format(date_string)
        
            cuerpo.foundation_date = d
            cuerpo.save()
        
        lemma = row[12]
        
        if lemma:
            # http://stackoverflow.com/questions/2872512/python-truncate-a-long-string
            cuerpo.lemma = lemma[:252] + (lemma[252:] and '...')
            # cuerpo.lemma = lemma
            cuerpo.save()

        alarm_central_phone = row[13]
        if alarm_central_phone:
            cuerpo.alarm_central_phone = alarm_central_phone

        date_string = row[17]

        if date_string:
            date_string = date_string.lower()
            
            for month_name, value in months:
                date_string = date_string.replace(month_name, str(value))
            
            m = re.search('(\d+)\D+(\d+)\D+(\d+)', date_string)
            if m:
                day = int(m.group(1))
                month = int(m.group(2))
                year = int(m.group(3))
                d = date(year, month, day)
                print date_string.encode('ascii', 'ignore')
                print d
            else:
                print 'No parseable, {0}'.format(date_string)
        
            cuerpo.decree_date = d
            cuerpo.save()


        '''
        foundation_date = models.DateField(blank=True, null=True)
        lemma = models.CharField(max_length=255)
        alarm_central_phone = models.CharField(max_length=100)
        communes = models.ManyToManyField('Commune', blank=True, null=True)
        decree_date = models.DateField(blank=True, null=True) # fecha decreto
    
        # De aca para abajo: Cosas pendientes y dudosas
        
        # TODO: logo
        cuer_npers_juri = models.IntegerField(blank=True, null=True) # No estamos seguros de para que es, borrar si no sirve para nada
        '''

    print 'Migrando Roles'
    cursor.execute("SELECT * FROM cargo")
    rows = cursor.fetchall()
    for row in rows:
        name = row[1]
        if name:
            role = Role()
            role.name = name
            role.save()
            print role

    print 'Migrando Usuarios'

    print 'Migrando Roles de Usuario'

if __name__ == '__main__':
    print datetime.now()
    main()


