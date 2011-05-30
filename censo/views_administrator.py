# coding: utf-8

from authentication import authorize

from censo.models import Cuerpo
from censo.models import Region

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect

# Show first stub
@authorize(roles=('administrator',))
def index(request):

    # Render the form
    return render_to_response('administrator/index.html', {}, context_instance=RequestContext(request),
        )
