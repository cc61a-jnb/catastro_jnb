# coding: utf-8

import logging

from utils import generic_edit
from authentication import authorize

from censo.forms import *
from censo.models import *

from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

from utils import generic_edit

# Show main form
@authorize()
def display_portada_form(request, cuerpo):
    try:
        portada_data = cuerpo.portadacuerpodata
        logging.info("Successfully fetched cuerpo:%s's portadacuerpodata for user:%s", cuerpo.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating cuerpo:%s's portadacuerpodata model for user:%s", cuerpo.old_id, request.user.username)
        portada_data = PortadaCuerpoData()
        # Add cuerpo to blank data
        portada_data.cuerpo = cuerpo
        portada_data.save()
        
    return generic_edit(request, portada_data, CuerpoPortadaForm, 'cuerpo/portada.html', reverse('cuerpo_general', kwargs={'cuerpo_id':cuerpo.old_id}), [[CuerpoOtherOfficial, cuerpo]])

# Show general info form
@authorize()
def display_general_form(request, cuerpo):
    general_data = None
    # Attempt to load previously submitted data
    try:
        general_data = cuerpo.cuerpogeneraldata
        logging.info("Successfully fetched cuerpo:%s's cuerpogeneraldata for user:%s", cuerpo.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating cuerpo:%s's cuerpogeneraldata model for user:%s", cuerpo.old_id, request.user.username)
        general_data = CuerpoGeneralData()
        # Add cuerpo to blank data
        general_data.cuerpo = cuerpo
        general_data.save()

    return generic_edit(request, general_data, CuerpoGeneralForm, 'cuerpo/general.html', reverse('cuerpo_anb', kwargs={'cuerpo_id':cuerpo.old_id}))

# Show ANB info form
@authorize()
def display_anb_form(request, cuerpo):
    anb_data = None
    # Attempt to load previously submitted data
    try:
        anb_data = cuerpo.cuerpoanbdata
        logging.info("Successfully fetched cuerpo:%s's cuerpoanbdata for user:%s", cuerpo.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating cuerpo:%s's cuerpoanbdata model for user:%s", cuerpo.old_id, request.user.username)
        anb_data = CuerpoANBData()
        # Add cuerpo to blank data
        anb_data.cuerpo = cuerpo
        anb_data.save()

    return generic_edit(request, anb_data, CuerpoANBForm, 'cuerpo/anb.html', reverse('cuerpo_infrastructure', kwargs={'cuerpo_id':cuerpo.old_id}))

# Show Infrastructure info form
@authorize()
def display_infrastructure_form(request, cuerpo):

    infrastructure_data = None
    # Attempt to load previously submitted data
    try:
        infrastructure_data = cuerpo.cuerpoinfrastructuredata
        logging.info("Successfully fetched cuerpo:%s's cuerpoinfrastructuredata for user:%s", cuerpo.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating cuerpo:%s's cuerpoinfrastructuredata model for user:%s", cuerpo.old_id, request.user.username)
        infrastructure_data = CuerpoInfrastructureData()
        # Add cuerpo to blank data
        infrastructure_data.cuerpo = cuerpo
        infrastructure_data.save()
        

    #call to generic function to show dynamic fields    
    return generic_edit(request, infrastructure_data, CuerpoInfrastructureForm, 'cuerpo/infrastructure.html', reverse('cuerpo_mayor_material', kwargs={'cuerpo_id':cuerpo.old_id}), [[CuerpoInfrastructureOtherOffices, cuerpo], [CuerpoElectGeneratorFixedBarracks, infrastructure_data]])
        
# Show Mayor Material Index
@authorize()
def display_mayor_material_index(request, cuerpo):
    
    # Get mayor material list
    mayor_material_list = cuerpo.cuerpomayormaterialdata_set.all()
    
    return render_to_response('cuerpo/mayor_material.html', {
                'instance': {'cuerpo':cuerpo},
                'mayor_material_list': mayor_material_list,
                'menu_titles': True,
                }, context_instance=RequestContext(request),
                )

# Show Mayor Material form
@authorize()
def edit_mayor_material_form(request, cuerpo, mayor_material_id):
    mayor_material_data = None
    # Attempt to load previously submitted data
    try:
        mayor_material_data = cuerpo.cuerpomayormaterialdata_set.get(pk=mayor_material_id)
        logging.info("Successfully fetched cuerpo:%s's portadacuerpodata for user:%s", cuerpo.old_id, request.user.username)
    except CuerpoMayorMaterialData.DoesNotExist:
        # Redirect to default mayor material
        logging.error("Requested mayor material data id:%s for cuerpo:%s doesn't exists, user:%s", mayor_material_id, cuerpo.id, request.user.username)
        request.flash['error'] = 'La planilla de material mayor consultada no existe'
        return redirect('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id)

    return generic_edit(request, mayor_material_data, CuerpoMayorMaterialForm, 'cuerpo/mayor_material_edit.html', reverse('cuerpo_mayor_material', kwargs={'cuerpo_id':cuerpo.old_id}), [[CuerpoMaterialMayorInstalledRadio, mayor_material_data], [CuerpoMaterialMayorPortableRadio, mayor_material_data], [CuerpoMaterialMayorAntenna, mayor_material_data], [CuerpoMaterialMayorGeneratorFixed, mayor_material_data], [CuerpoMaterialMayorGeneratorPort, mayor_material_data]], [('company', Company.objects.filter(cuerpo=cuerpo))])

# Add New Mayor Material form
@authorize()
def add_new_mayor_material(request, cuerpo):
    logging.info("Creating cuerpo:%s's new mayor_material form for user:%s", cuerpo.old_id, request.user.username)
    mayor_material_data = CuerpoMayorMaterialData()
    mayor_material_data.cuerpo = cuerpo
    
    return generic_edit(request, mayor_material_data, CuerpoMayorMaterialForm, 'cuerpo/mayor_material_edit.html', reverse('cuerpo_mayor_material', kwargs={'cuerpo_id':cuerpo.old_id}), [[CuerpoMaterialMayorInstalledRadio, mayor_material_data],[CuerpoMaterialMayorPortableRadio, mayor_material_data], [CuerpoMaterialMayorAntenna, mayor_material_data], [CuerpoMaterialMayorGeneratorFixed, mayor_material_data], [CuerpoMaterialMayorGeneratorPort, mayor_material_data]], [('company', Company.objects.filter(cuerpo=cuerpo))])
        

# Remove Selected Material form
@authorize()
def remove_mayor_material(request, cuerpo, mayor_material_id):
    if request.method == 'POST':
        mayor_material_data = None

        try:
            mayor_material_data = cuerpo.cuerpomayormaterialdata_set.get(pk=mayor_material_id)
            logging.info("Successfully fetched cuerpo:%s's mayor_material:%s for user:%s", cuerpo.old_id, mayor_material_id, request.user.username)
        # The id provided in the url does not exist
        except CuerpoMayorMaterialData.DoesNotExist:
            # Redirect to default mayor material
            request.flash['error'] = 'La planilla de material mayor consultada no existe'
            logging.error("Requested mayor material data id:%s for cuerpo:%s doesn't exists, user:%s", mayor_material_id, cuerpo.id, request.user.username)
            return redirect('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id)
        
        logging.info("Deleting mayor material data object id:%s for cuerpo:%s, user:%s", mayor_material_data.id, cuerpo.id, request.user.username)
        mayor_material_data.delete()
        request.flash['success'] = "Se ha eliminado la ficha seleccionada satisfactoriamente"
    
    return redirect('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id)

# Show Alarm Central form
@authorize()
def display_alarm_central_form(request, cuerpo):
    alarm_central_cuerpo_data = None
    # Attempt to load previously submitted data
    try:
        alarm_central_cuerpo_data = cuerpo.cuerpoalarmcentraldata
        logging.info("Successfully fetched cuerpo:%s's cuerpoalarmcentraldata for user:%s", cuerpo.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating cuerpo:%s's cuerpoalarmcentraldata model for user:%s", cuerpo.old_id, request.user.username)
        alarm_central_cuerpo_data = CuerpoAlarmCentralData()
        # Add cuerpo to blank data
        alarm_central_cuerpo_data.cuerpo = cuerpo
        alarm_central_cuerpo_data.save() 
   
    #call to generic function to show dynamic fields    
    return generic_edit(request, alarm_central_cuerpo_data, CuerpoAlarmCentralForm, 'cuerpo/alarm_central.html', reverse('cuerpo_service_acts', kwargs={'cuerpo_id':cuerpo.old_id}), [[CuerpoAlarmCentralBaseRadioEq, cuerpo]])


# Show Service acts form
@authorize()
def display_service_acts_form(request, cuerpo):
    service_acts_data = None
    # Attempt to load previously submitted data
    try:
        service_acts_data = cuerpo.cuerposerviceactsdata
        logging.info("Successfully fetched cuerpo:%s's cuerposerviceactsdata for user:%s", cuerpo.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating cuerpo:%s's cuerposerviceactsdata model for user:%s", cuerpo.old_id, request.user.username)
        service_acts_data = CuerpoServiceActsData()
        # Add cuerpo to blank data
        service_acts_data.cuerpo = cuerpo
        service_acts_data.save()

    return generic_edit(request, service_acts_data, CuerpoServiceActsForm, 'cuerpo/service_acts.html', reverse('index'))
