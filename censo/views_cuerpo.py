# coding: utf-8

import logging
from utils import authorize, generic_edit
from censo.forms import *
from censo.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import inlineformset_factory
from utils import generic_edit

# Show main form
@authorize(roles=('cuerpo',))
def display_portada_form(request):
    profile = request.user.get_profile()
    
    cuerpo = profile.company.cuerpo
    
    try:
        portada_data = cuerpo.portadacuerpodata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        portada_data = PortadaCuerpoData()
        # Add cuerpo to blank data
        portada_data.cuerpo = cuerpo
        portada_data.save()
        
    return generic_edit(request, portada_data, CuerpoPortadaForm, 'cuerpo/first_page.html', reverse('catastro_jnb.censo.views_cuerpo.display_general_form'), [[CuerpoOtherOfficial, cuerpo]])

# Show general info form
@authorize(roles=('cuerpo',))
def display_general_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    general_data = None
    # Attempt to load previously submitted data
    try:
        general_data = cuerpo.cuerpogeneraldata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        general_data = CuerpoGeneralData()
        # Add cuerpo to blank data
        general_data.cuerpo = cuerpo
        general_data.save()

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CuerpoGeneralForm(request.POST, instance=general_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/cuerpo/anb')
        # Else render the form again
        else:
            return render_to_response('cuerpo/second_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoGeneralForm(instance=general_data)

    # Render the form
    return render_to_response('cuerpo/second_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

# Show ANB info form
@authorize(roles=('cuerpo',))
def display_anb_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    anb_data = None
    # Attempt to load previously submitted data
    try:
        anb_data = cuerpo.cuerpoanbdata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        anb_data = CuerpoANBData()
        # Add cuerpo to blank data
        anb_data.cuerpo = cuerpo
        anb_data.save()

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CuerpoANBForm(request.POST, instance=anb_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return redirect('cuerpo_infrastructure')
        # Else render the form again
        else:
            return render_to_response('cuerpo/third_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoANBForm(instance=anb_data)

    # Render the form
    return render_to_response('cuerpo/third_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

# Show Infrastructure info form
@authorize(roles=('cuerpo',))
def display_infrastructure_form(request):
    profile = request.user.get_profile()

    cuerpo = profile.company.cuerpo

    infrastructure_data = None
    # Attempt to load previously submitted data
    try:
        infrastructure_data = cuerpo.cuerpoinfrastructuredata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        infrastructure_data = CuerpoInfrastructureData()
        # Add cuerpo to blank data
        infrastructure_data.cuerpo = cuerpo
        infrastructure_data.save()

    #call to generic function to show dynamic fields    
    return generic_edit(request, infrastructure_data, CuerpoInfrastructureForm, 'cuerpo/fourth_page.html', reverse('catastro_jnb.censo.views_cuerpo.display_mayor_material_index'), [[CuerpoInfrastructureOtherOffices, cuerpo]])

        
# Show Mayor Material Index
@authorize(roles=('cuerpo',))
def display_mayor_material_index(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    
    # Get mayor material list
    mayor_material_list = cuerpo.cuerpomayormaterialdata_set.all()
    
    return render_to_response('cuerpo/fifth_page.html', {
                'cuerpo': cuerpo,
                'mayor_material_list': mayor_material_list,
                }, context_instance=RequestContext(request),
                )

# Show Mayor Material form
@authorize(roles=('cuerpo',))
def edit_mayor_material_form(request, mayor_material_id):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    mayor_material_data = None
    # Attempt to load previously submitted data
    try:
        mayor_material_data = cuerpo.cuerpomayormaterialdata_set.get(pk=mayor_material_id)
    except CuerpoMayorMaterialData.DoesNotExist:
        # Redirect to default mayor material
        logging.error("Requested mayor material data id:%d for cuerpo:%d doesn't exists", mayor_material_id, cuerpo.id)
        request.flash['error'] = 'La planilla de material mayor consultada no existe'
        return redirect('cuerpo_mayor_material')

    return generic_edit(request, mayor_material_data, CuerpoMayorMaterialForm, 'cuerpo/fifth_page_edit.html', reverse('catastro_jnb.censo.views_cuerpo.display_mayor_material_index'), [[CuerpoMaterialMayorInstalledRadio, mayor_material_data], [CuerpoMaterialMayorPortableRadio, mayor_material_data], [CuerpoMaterialMayorAntenna, mayor_material_data]], ['company', Company.objects.filter(cuerpo=cuerpo)])

# Add New Mayor Material form
@authorize(roles=('cuerpo',))
def add_new_mayor_material(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    mayor_material_data = CuerpoMayorMaterialData()
    mayor_material_data.cuerpo = cuerpo
    
    return generic_edit(request, mayor_material_data, CuerpoMayorMaterialForm, 'cuerpo/fifth_page_edit.html', reverse('catastro_jnb.censo.views_cuerpo.display_mayor_material_index'), [[CuerpoMaterialMayorInstalledRadio, mayor_material_data],[CuerpoMaterialMayorPortableRadio, mayor_material_data], [CuerpoMaterialMayorAntenna, mayor_material_data]], ['company', Company.objects.filter(cuerpo=cuerpo)])
        

# Remove Selected Material form
@authorize(roles=('cuerpo',))
def remove_mayor_material(request, mayor_material_id):
    if request.method == 'POST':
        profile = request.user.get_profile()
        cuerpo = profile.company.cuerpo
        mayor_material_data = None

        try:
            mayor_material_data = cuerpo.cuerpomayormaterialdata_set.get(pk=mayor_material_id)
        # The id provided in the url does not exist
        except CuerpoMayorMaterialData.DoesNotExist:
            # Redirect to default mayor material
            request.flash['error'] = 'La planilla de material mayor consultada no existe'
            logging.error("Requested mayor material data id:%d for cuerpo:%d doesn't exists", mayor_material_id, cuerpo.id)
            return redirect('cuerpo_mayor_material')
        
        logging.info("Deleting mayor material data object id:%d for cuerpo:%d", mayor_material_data.id, cuerpo.id)
        mayor_material_data.delete()
        request.flash['success'] = "Se ha eliminado la ficha seleccionada satisfactoriamente"
        return redirect('cuerpo_mayor_material')
    else:
        return redirect('cuerpo_mayor_material')

# Show Alarm Central form
@authorize(roles=('cuerpo',))
def display_alarm_central_form(request):
    profile = request.user.get_profile()

    cuerpo = profile.company.cuerpo

    alarm_central_cuerpo_data = None
    # Attempt to load previously submitted data
    try:
        alarm_central_cuerpo_data = cuerpo.cuerpoalarmcentraldata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        alarm_central_cuerpo_data = CuerpoAlarmCentralData()
        # Add cuerpo to blank data
        alarm_central_cuerpo_data.cuerpo = cuerpo
        alarm_central_cuerpo_data.save() 
   
    #call to generic function to show dynamic fields    
    return generic_edit(request, alarm_central_cuerpo_data, CuerpoAlarmCentralForm, 'cuerpo/sixth_page.html', reverse('catastro_jnb.censo.views_cuerpo.display_service_acts_form'), [[CuerpoAlarmCentralBaseRadioEq, cuerpo]])


# Show Service acts form
@authorize(roles=('cuerpo',))
def display_service_acts_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    service_acts_data = None
    # Attempt to load previously submitted data
    try:
        service_acts_data = cuerpo.cuerposerviceactsdata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        service_acts_data = CuerpoServiceActsData()
        # Add cuerpo to blank data
        service_acts_data.cuerpo = cuerpo
        service_acts_data.save()

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CuerpoServiceActsForm(request.POST, instance=service_acts_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/cuerpo/serviceacts')
        # Else render the form again
        else:
            return render_to_response('cuerpo/seventh_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoServiceActsForm(instance=service_acts_data)

    # Render the form
    return render_to_response('cuerpo/seventh_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )
