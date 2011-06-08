# coding: utf-8

import logging

from functools import wraps

from censo.models import Cuerpo
from censo.models import Company

from django.conf import settings
from django.db import connections
from django.shortcuts import redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, check_password

# Check if user has the role required to the decorated view
class authorize(object):
    """
    Checks if user has permission over requested cuerpo_id or company_id,
    if not then fallback to index.
    Returns fetched Cuerpo or Company objects to decorated function
    as cuerpo or company kwargs, and delete company_id and/or cuerpo_id

    roles tuple is optional and can contain any of these: 
    'administrator', 'regional_operations_manager', 'cuerpo', 'company'
    e.g. @authorize(roles=('administrator','regional_operations_manager',))
    """
    def __init__(self, roles=()):
        self.roles = roles

    def __call__(self, func):

        @wraps(func)
        def wrap(request, *args, **kwargs):
            # If user isn't authenticated
            if not request.user.is_authenticated():
                logging.info("User not authenticated tried to access the system")
                request.flash['notice'] = 'Por favor inicie sesión primero'
                return redirect('login')

            # define basic data
            profile = request.user.get_profile()
            cuerpo_id = kwargs.get('cuerpo_id', None)
            company_id = kwargs.get('company_id', None)
            cursor = connections['principal'].cursor()

            # check role if defined at decorator instantiation
            if self.roles:
                role_name = None
                # assign current role to human readable format
                if profile.is_administrator():
                    role_name = 'administrator'
                elif profile.is_regional_operations_manager():
                    role_name = 'regional_operations_manager'
                elif profile.is_cuerpo_manager():
                    role_name = 'cuerpo'
                elif profile.is_company_manager():
                    role_name = 'company'

                # If user doesn't have access, redirect
                if not (role_name in self.roles):
                    request.flash['error'] = 'Usted no tiene permisos para realizar esta acción'
                    logging.info("User %s doesn't have permission to access %s", request.user.username, request.path)
                    return redirect('index')

            # deliver cuerpo if requested
            if cuerpo_id:
                cuerpo = Cuerpo.fetch_from_db(cursor, cuerpo_id)

                if not cuerpo:
                    logging.info("Cuerpo:%s doesn't exist", cuerpo_id) # why %s: http://stackoverflow.com/questions/2796178/error-url-redirection
                    request.flash["error"] = 'El cuerpo que ha ingresado no existe'
                    cursor.close()
                    return redirect('index')

                # now we must check user's permissions
                if not profile.has_cuerpo_permission(cursor, cuerpo):
                    logging.warning("User:%s unauthorized to access Cuerpo:%s information", profile.old_id, cuerpo_id)
                    request.flash["error"] = 'No tiene permiso para acceder a la información del cuerpo seleccionado'
                    cursor.close()
                    return redirect('index')
                
                # replace cuerpo_id with full cuerpo object
                del kwargs['cuerpo_id']
                kwargs['cuerpo'] = cuerpo

            # deliver company if requested
            if company_id:
                company = Company.fetch_from_db(cursor, company_id)

                if not company:
                    logging.info("Company:%s doesn't exist", company_id) # why %s: http://stackoverflow.com/questions/2796178/error-url-redirection
                    request.flash["error"] = 'La compañía que ha ingresado no existe'
                    cursor.close()
                    return redirect('index')

                # now we must check user's permissions
                if not profile.has_company_permission(cursor, company):
                    logging.warning("User:%s unauthorized to access Company:%s information", profile.old_id, company_id)
                    request.flash["error"] = 'No tiene permiso para acceder a la información de la compañía seleccionada'
                    cursor.close()
                    return redirect('index')
                
                # replace company_id with full company object
                del kwargs['company_id']
                kwargs['company'] = company
            
            # user has permission over cuerpo
            cursor.close()
            
            return func(request, *args, **kwargs)

        return wrap


class JNBBackend:
    """
    Authenticate against the JNB Main Database
    """

    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        user = None
        cursor = connections['postfix'].cursor()

        # username needs to be transformed into email
        # reference: http://stackoverflow.com/questions/3217682/checking-validity-of-email-in-django-python
        try:
            validate_email(username)
        except ValidationError:
            username = u'@'.join((username, u'bomberos.cl',))

        query = "SELECT correopk FROM mailbox WHERE username = %s AND password = %s"
        params = (username, password,)
        
        cursor.execute(query, params)
        postfix_data = cursor.fetchone()

        if postfix_data is None:
            # The username/password do not match
            logging.info("Username/password for user %s do not match", username)
            cursor.close()
            return None
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            logging.info("The user (%s) is logging for the first time, initializing data", username)
            user = User(username=username, password=password)
            user.is_staff = False
            user.is_superuser = False
            user.save()

        profile = user.get_profile()

        # If for some reason the user does not have a uid in the database, burn everything and abort
        if postfix_data[0] is None:
            logging.info("User %s does not have a correopk", username)
            profile.delete()
            user.delete()
            cursor.close()
            return None
            
        correo_pk = postfix_data[0]
        
        # Try and get the user_id from usu_mail
        
        query = "SELECT fk_usu FROM mail_usu WHERE fk_mail = %s"
        params = (correo_pk,)
        cursor.execute(query, params)

        user_data = cursor.fetchone()
        if not user_data:
            logging.info("User %s with correopk %s does not exist in table 'mail_usu'" % (username, correo_pk))
            profile.delete()
            user.delete()
            cursor.close()
            return None
            
        profile.old_id = user_data[0]
        cursor.close()

        cursor = connections['principal'].cursor()

        # First of all, determine user role
        profile.determine_role(cursor)

        # If user is not reg. op. manager, fetch company
        if not profile.is_regional_operations_manager():
            # Try and get the user company
            query = "SELECT usu_fk_cia FROM usuarios WHERE usu_id = %s"
            params = (profile.old_id,)
            cursor.execute(query, params)

            user_data = cursor.fetchone()
            
            if not user_data:
                # The user does not exist in the principal database (broken foreign key)
                # As always, burn and quit
                logging.error("User %s with id %s does not exist in table 'usuarios'", username, profile.old_id)
                profile.delete()
                user.delete()
                cursor.close()
                return None
                
            old_company_id = user_data[0]
            
            company = Company.fetch_from_db(cursor, old_company_id)    
            
            if not company:
                logging.error("User %s associated company is foreign key broken (in commune, province, region, or cuerpo)", username)
                profile.delete()
                user.delete()
                cursor.close()
                return None
                
            profile.company = company
        
        profile.save()
        user.save()

        cursor.close()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


