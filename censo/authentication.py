import logging
from censo.models import *
from django.conf import settings
from django.db import connections
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, check_password

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
            logging.info("User %s with correopk %d does not exist in table 'mail_usu'" % (username, correo_pk))
            profile.delete()
            user.delete()
            cursor.close()
            return None
            
        profile.old_id = user_data[0]
        cursor.close()

        # Try and get the user company
        cursor = connections['principal'].cursor()

        query = "SELECT usu_fk_cia FROM usuarios WHERE usu_id = %s"
        params = (profile.old_id,)
        cursor.execute(query, params)

        user_data = cursor.fetchone()
        
        if not user_data:
            # The user does not exist in the principal database (broken foreign key)
            # As always, burn and quit
            logging.error("User %s with id %d does not exist in table 'usuarios'" % (username, profile.old_id))
            profile.delete()
            user.delete()
            cursor.close()
            return None
            
        old_company_id = user_data[0]
        
        company = Company.fetch_from_db(cursor, old_company_id)    
        
        if not company:
            logging.error("User %s associated company is foreign key broken (in commune, province, region, or cuerpo)" % username)
            profile.delete()
            user.delete()
            cursor.close()
            return None
            
        profile.company = company
        profile.determine_role(cursor)
        
        profile.save()
        user.save()

        cursor.close()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
