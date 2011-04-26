from django.db import models
from . import Role, UserProfile

class UserHasRole(models.Model):
    profile = models.ForeignKey(UserProfile)
    role = models.ForeignKey(Role)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cuerpo = models.ForeignKey('Cuerpo', blank = True, null = True)
    
    def __unicode__(self):
        return u''.join((self.profile.user.username,' - ',str(self.role)))

    class Meta:
        ordering = ['profile', 'role']
        app_label = 'censo'
