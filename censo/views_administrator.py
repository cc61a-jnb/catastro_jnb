# coding: utf-8

import logging

from authentication import authorize

from censo.models import Cuerpo
from censo.models import Region
from censo.models import Administrator

from censo.utils import get_menu_data

from django.db import connections
from django.template import RequestContext
from django.shortcuts import redirect
from django.shortcuts import render_to_response

from censo.forms import AdministratorResultsCuerpoForm

# Show first stub
@authorize(roles=('administrator',))
def index(request):

    menu_titles, main_menu_choices, user_permission_instance = request.user.get_profile().get_menu()

    # Render the form
    return render_to_response('administrator/index.html', {
        'menu_titles': menu_titles[:-1],
        'main_menu_choices': main_menu_choices,
        'user_permission_instance': user_permission_instance
    }, context_instance=RequestContext(request),
        )
        
@authorize(roles=('administrator',))
def results_cuerpo(request):
    form = AdministratorResultsCuerpoForm(request.GET)
    cuerpo_list = [] # soon to be filled if form is submitted
    
    # verify if form has been sent
    if form.is_valid():
        # get region if selected
        region = form.cleaned_data["region"]
        if region:
            # fetch all cuerpos from db
            cursor = connections["principal"].cursor()
            cuerpo_data_list = Region.fetch_all_related(cursor, region.old_id)
            for cuerpo_data in cuerpo_data_list:
                # try first to get cuerpo from our records
                try:
                    cuerpo = Cuerpo.objects.get(old_id=cuerpo_data["id"])
                    cuerpo_list.append(cuerpo)
                except Cuerpo.DoesNotExist:
                    cuerpo = Cuerpo.fetch_from_db(cursor, cuerpo_data["id"])
                    if cuerpo: # is null in case of virtual cuerpo or inconsistent db
                        cuerpo.save()
                        cuerpo_list.append(cuerpo)

    return render_to_response('administrator/results_cuerpo.html', {
        'form': form,
        'cuerpo_list': cuerpo_list,
        'menu_titles': True,
    }, context_instance=RequestContext(request))

@authorize(roles=('administrator',))
def results_company(request):
    company_list = None

    # check if user has specified a cuerpo_id
    cuerpo_id = request.GET.get('cuerpo_id', None)
    if cuerpo_id:
        # try first to get cuerpo from our records
        try:
            cuerpo = Cuerpo.objects.get(old_id=cuerpo_id)
        except Cuerpo.DoesNotExist:
            # fetch cuerpo from db
            cursor = connections["principal"].cursor()
            cuerpo = Cuerpo.fetch_from_db(cursor, cuerpo_id)
            if cuerpo: # can null in case of virtual cuerpo or inconsistent db
                cuerpo.save()
            else:
                request.flash['error'] = "El cuerpo que ha seleccionado no existe en los registros"
                logging.error("Requested cuerpo:%s does not exist", cuerpo_id)
                return redirect('administrator_results_company')
        
        company_list = cuerpo.cuerpo_company.all()

    menu_titles, main_menu_choices, user_permission_instance = request.user.get_profile().get_menu()
    # Render the form
    return render_to_response('administrator/results_company.html', {
        'company_list': company_list,
        'menu_titles': menu_titles[:-1],
        'main_menu_choices': main_menu_choices,
        'user_permission_instance': user_permission_instance
        }, context_instance=RequestContext(request),
        )
