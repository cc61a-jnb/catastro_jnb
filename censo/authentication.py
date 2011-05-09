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

        query = "SELECT id_usu FROM mailbox WHERE username = %s AND password = %s"
        params = (username, password,)
        
        cursor.execute(query, params)
        user_data = cursor.fetchone()

        # if the credentials are correct
        if user_data:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                logging.info("The user (%s) is logging for the first time, initializing data", username)
                user = User(username=username, password=password)
                user.is_staff = False
                user.is_superuser = False
                user.save()

            profile = user.get_profile()

            # must update old_id in order to retrieve user roles
            profile.old_id = user_data[0]

            # cursor = connections['principal'].cursor()

            # query = "SELECT * FROM usuarios WHERE usu_id = %s"
            # params = (user_data[mailbox_usu_id_index],)

            # cursor.execute(query, params)

            # user_data = cursor.fetchone()

            # if user_data:
            #     try:
            #         profile.current_role = Role.objects.get(old_id = user_data[16])
            #     except: # error, el usuario no tiene rol
            #         logging.error("The user (%s) doesn't have roles assigned", username)

            #     try:
            #         company_id = user_data[14]
            #         profile.company = Company.objects.get(old_id = company_id)
            #     except:
            #         logging.error("The user (%s) doesn't have a company assigned", username)

            #     try:
            #         gender = user_data[19]
            #         if gender:
            #             profile.gender = user_data[19][0]
            #         else:
            #             profile.gender = 'M'
            #     except: 
            #         logging.error("Can't access user (%s) gender data", username)
            # else:
            #     logging.info("The user (%s) doensn't have information in the principal database", username)
            
            profile.save()
            user.save()

            cursor.close()
            return user

        cursor.close()
        return None
        

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
