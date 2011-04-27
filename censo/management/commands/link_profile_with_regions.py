# coding: utf-8

from django.core.management.base import NoArgsCommand
from censo.models import Region
from censo.models import UserProfile

class UnknownRegionException(Exception):
    pass

class Command(NoArgsCommand):

    help = "Run this command to link regions with profiles for region operations managers"

    option_list = NoArgsCommand.option_list

    def handle_noargs(self, **options):
    
        profiles = UserProfile.objects.filter(roles__name__contains='Jefe Operaciones')
        
        # exclude old profiles no longer being regional operations manager
        current_profiles = [p for p in profiles if p.latest_role().is_regional_operations_manager()]
        
        for profile in current_profiles:
            role = profile.latest_role()
            if "Primera Region" in role.name:
                profile.region = Region.objects.get(number=1)
            elif "Segunda Region" in role.name:
                profile.region = Region.objects.get(number=2)
            elif "Tercera Region" in role.name:
                profile.region = Region.objects.get(number=3)
            elif "Cuarta Region" in role.name:
                profile.region = Region.objects.get(number=4)
            elif "Quinta Region" in role.name:
                profile.region = Region.objects.get(number=5)
            elif "Sexta Region" in role.name:
                profile.region = Region.objects.get(number=6)
            elif "Septima Region" in role.name:
                profile.region = Region.objects.get(number=7)
            elif "Octava Region" in role.name:
                profile.region = Region.objects.get(number=8)
            elif "Novena Region" in role.name:
                profile.region = Region.objects.get(number=9)
            elif "Decima Region" in role.name:
                profile.region = Region.objects.get(number=10)
            elif "Undecima Region" in role.name:
                profile.region = Region.objects.get(number=11)
            elif "Duodecima Region" in role.name:
                profile.region = Region.objects.get(number=12)
            elif "Región Metrop." in role.name:
                profile.region = Region.objects.get(number=13)
            else: # TODO: add missing regions
                raise UnknownRegionException
            profile.save()
            
            
            
