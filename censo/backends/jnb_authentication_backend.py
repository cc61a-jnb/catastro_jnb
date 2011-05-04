from censo.models import *

class JnbAuthenticationBackend:
    '''
    Custom authentication against the JNB database
    http://docs.djangoproject.com/en/1.2/topics/auth/#writing-an-authentication-backend 
    '''
    def authenticate(self, username, password):
        try:
            profile = UserProfile.objects.get(user__username = username)
            return profile.user
        except:
            password = User.objects.make_random_password()
            
            user = User.objects.create_user(username, email, password)
            user.is_active = True
            user.save()
            profile = user.get_profile()
            profile.facebook_name = facebook_name
            profile.save()
            
            send_facebook_registration_mail(user)
            return user
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except:
            return None
