# coding: utf-8

from utils import authorize

from censo.models import Cuerpo
from censo.models import Region

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

# Show first stub
@authorize(roles=('regional_operations_manager',))
def basic_view(request):
    profile = request.user.get_profile()
    region = profile.region # this shouldn't fail
    
    # get all cuerpos which belong to this region
    cuerpos = Cuerpo.objects.filter(commune__province__region=region)

    # Render the form
    return render_to_response('regional_operations_manager/basic.html', {
            'cuerpos': cuerpos,
            }, context_instance=RequestContext(request),
        )
