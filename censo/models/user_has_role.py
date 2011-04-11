from django.db import models
from . import Role, UserProfile

class UserHasRole(models.Model):
    profile = models.ForeignKey(UserProfile)
    role = models.ForeignKey(Role)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['profile', 'role']
        app_label = 'censo'
