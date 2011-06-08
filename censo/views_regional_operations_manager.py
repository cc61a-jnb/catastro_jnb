# coding: utf-8

from authentication import authorize

from censo.models import Cuerpo
from censo.models import Region, Administrator

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect

# Show first stub
@authorize()
def index(request, region):

    menu_titles, main_menu_choices, user_permission_instance = request.user.get_profile().get_menu()

    # Render the form
    return render_to_response('regional_operations_manager/index.html', {
        'menu_titles': menu_titles[:-1],
        'main_menu_choices': main_menu_choices,
        'user_permission_instance': user_permission_instance
    }, context_instance=RequestContext(request),
        )
