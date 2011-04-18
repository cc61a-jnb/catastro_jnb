from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from . import Occupation, Company, Role

class UserProfile(models.Model):
    old_id = models.IntegerField(default = 0)
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length = 100, default = '')
    first_last_name = models.CharField(max_length = 40, default = '')
    second_last_name = models.CharField(max_length = 40, default = '')
    rut = models.CharField(max_length = 10, default = '')
    address = models.CharField(max_length = 255, default = '')
    phone = models.CharField(max_length = 40, default = '')
    cell_phone = models.CharField(max_length = 40, default = '')
    work_phone = models.CharField(max_length = 40, default = '')
    occupation = models.ForeignKey(Occupation, blank = True, null = True)
    work_address = models.CharField(max_length = 255, default = '')
    company = models.ForeignKey(Company, blank = True, null = True)
    roles = models.ManyToManyField(Role, through = 'UserHasRole')
    current_role = models.ForeignKey(Role, related_name='+', blank = True, null = True)
    gender = models.CharField(max_length = 1)

    def __unicode__(self):
        return "Perfil de %s" % self.user
        
    def latest_role(self):
        roles = self.roles.order_by('old_id')
        if roles:
            return roles[0]
        else:
            return None

    class Meta:
        ordering = ['user']
        app_label = 'censo'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user = instance)

post_save.connect(create_user_profile, sender = User)
