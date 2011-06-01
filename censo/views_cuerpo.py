# coding: utf-8

import logging

from utils import generic_edit
from authentication import authorize

from censo.forms import *
from censo.models import *

from django.db import connections
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import inlineformset_factory

# Show main form
@authorize()
def display_portada_form(request, cuerpo):
    
    try:
        portada_data = cuerpo.portadacuerpodata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        portada_data = PortadaCuerpoData()
        # Add company to blank data
        portada_data.cuerpo = cuerpo
        portada_data.save()
    
    #previene que se muestren los errores de envio al presionar el botón agregar otro
    prevent_validation_error = False

    AddOtherRoleCuerpoFormSet = inlineformset_factory(Cuerpo, CuerpoOtherOfficial, extra=0, can_delete=True)
    # companies = cuerpo
    # TODO: add company selector

    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST
        main_form = CuerpoPortadaForm(request.POST, instance=portada_data)

        if 'add_other_official' in request.POST:
            
            # Get the data from POST
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', data=request.POST, instance=cuerpo)
            prevent_validation_error = True
            
            # Saving Added Rows
            for form in new_other_official.forms:
                if form.has_changed():
                    if form.is_valid():
                        form.save()
            ### Al usar sólo el request.POST para obtener y recargar los datos
            ### del formulario, los datos no tenían id de la base de datos (pues
            ### nunca eran cargados de ahí), luego al hacer cualquier modificación
            ### sobre éstos, eran considerados nuevos datos y se guardaban en la BD
            ### junto con la versión antigua (duplicación de líneas).
            ### Ahora estamos creando líneas vacías en la BD al hacer el agregar,
            ### para cargar de la base de datos. Toda línea que quede vacía después de
            ### llenar los datos debería eliminarse al hacer el guardado del formulario
            ### completo.
            
            # Create new empty line in DB
            coo_new = CuerpoOtherOfficial(cuerpo=cuerpo, role_name='', person_name='')
            coo_new.save()
            
            # Reload data from DB
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official',  instance=cuerpo)
            if main_form.is_valid():
                main_form.save()
        
        elif 'delete_other_official' in request.POST:
            prevent_validation_error = True
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', data=request.POST, instance=cuerpo)
            
            # Saving Changed Rows
            for form in new_other_official.forms:
                if form.is_valid():
                    if form.has_changed():
                        form.save()
                            
            # Then we delete the appropiate rows
            for form in new_other_official.deleted_forms:
                if form.is_valid():
                    coo_del = form.cleaned_data['id']
                    coo_del.delete()
                    
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', instance=cuerpo)
            
            if main_form.is_valid():
                main_form.save()
           
        else:
             # A form bound to the POST data
            main_form = CuerpoPortadaForm(request.POST, instance=portada_data)
            # If the form is correctly validated
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', data=request.POST, instance=cuerpo)
            if new_other_official.is_valid() and main_form.is_valid():      
                for fm in new_other_official.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            fm.save()
                main_form.save()
                ## Delete empty entries
                query = CuerpoOtherOfficial.objects.filter(cuerpo=cuerpo)
                for q in query:
                    if q.role_name == '' and q.person_name == '':
                        q.delete()
                # Redirect after POST
                return redirect('cuerpo_general', cuerpo_id=cuerpo.old_id)
            # Else render the form again
            else:
                return render_to_response('cuerpo/portada.html', {
                    'form': main_form,
                    'cuerpo': cuerpo,
                    'other_official': new_other_official,
                    }, context_instance=RequestContext(request),
                    )
        # A form bound to the POST data
        main_form = CuerpoPortadaForm(request.POST, instance=portada_data)

    else:
        # If the form hasn't been submitted
        new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official',instance=cuerpo)
    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    main_form = CuerpoPortadaForm(instance=portada_data)

    # Render the form
    return render_to_response('cuerpo/portada.html', {
            'form': main_form,
            'cuerpo': cuerpo,
            'other_official': new_other_official,
            }, context_instance=RequestContext(request),
        )

# Show general info form
@authorize()
def display_general_form(request, cuerpo):
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
            return redirect('cuerpo_anb', cuerpo_id=cuerpo.old_id)
        # Else render the form again
        else:
            return render_to_response('cuerpo/general.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoGeneralForm(instance=general_data)

    # Render the form
    return render_to_response('cuerpo/general.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

# Show ANB info form
@authorize()
def display_anb_form(request, cuerpo):
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
            return redirect('cuerpo_infrastructure', cuerpo_id=cuerpo.old_id)
        # Else render the form again
        else:
            return render_to_response('cuerpo/anb.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoANBForm(instance=anb_data)

    # Render the form
    return render_to_response('cuerpo/anb.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

# Show Infrastructure info form
@authorize()
def display_infrastructure_form(request, cuerpo):

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


    #previene que se muestren los errores de envio al presionar el botón agregar otro
    prevent_validation_error = False

    AddOtherOfficesFormSet = inlineformset_factory(Cuerpo, CuerpoInfrastructureOtherOffices, extra=0, can_delete=True)
    
    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST

        if 'add_other_offices' in request.POST:
            
            # Get the data from POST
            new_other_offices = AddOtherOfficesFormSet(prefix='other_offices', data=request.POST, instance=cuerpo)
            prevent_validation_error = True
            
            # Saving Added Rows
            for form in new_other_offices.forms:
                if form.has_changed():
                    if form.is_valid():
                        form.save()
        
            
            # Create new empty line in DB
            cioo_new = CuerpoInfrastructureOtherOffices(cuerpo=cuerpo, role_name='')
            cioo_new.save()
            
            # Reload data from DB
            new_other_offices = AddOtherOfficesFormSet(prefix='other_offices',  instance=cuerpo)
        
        elif 'delete_other_offices' in request.POST:
            prevent_validation_error = True
            new_other_offices = AddOtherOfficesFormSet(prefix='other_offices', data=request.POST, instance=cuerpo)
            
            # Saving Changed Rows
            for form in new_other_offices.forms:
                if form.is_valid():
                    if form.has_changed():
                        form.save()
                            
            # Then we delete the appropiate rows
            for form in new_other_offices.deleted_forms:
                if form.is_valid():
                    coo_del = form.cleaned_data['id']
                    coo_del.delete()
                    
            new_other_offices = AddOtherOfficesFormSet(prefix='other_offices', instance=cuerpo)
           
        else:
             # A form bound to the POST data
            z = dict(request.POST, **request.FILES)
	    form = CuerpoInfrastructureForm(request.POST, request.FILES, instance=infrastructure_data)
            # If the form is correctly validated
            new_other_offices = AddOtherOfficesFormSet(prefix='other_offices', data=request.POST, instance=cuerpo)
            if new_other_offices.is_valid() and form.is_valid():      
                for fm in new_other_offices.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            fm.save()
                form.save()
                ## Delete empty entries
                query = CuerpoInfrastructureOtherOffices.objects.filter(cuerpo=cuerpo)
                for q in query:
                    if q.role_name == '':
                        q.delete()
                # Redirect after POST
                return redirect('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id)
            # Else render the form again
            else:
                return render_to_response('cuerpo/infrastructure.html', {
                    'form': form,
                    'cuerpo': cuerpo,
                    'other_offices': new_other_offices,
                    }, context_instance=RequestContext(request),
                    )
        # A form bound to the POST data
	form = CuerpoInfrastructureForm(request.POST, request.FILES, instance=infrastructure_data)

    else:
        # If the form hasn't been submitted
        new_other_offices = AddOtherOfficesFormSet(prefix='other_offices',instance=cuerpo)
     
    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoInfrastructureForm(instance=infrastructure_data)

    # Render the form
    return render_to_response('cuerpo/infrastructure.html', {
            'form': form,
            'cuerpo': cuerpo,
            'other_offices': new_other_offices,
            }, context_instance=RequestContext(request),
        )
        
# Show Mayor Material Index
@authorize()
def display_mayor_material_index(request, cuerpo):
    
    # Get mayor material list
    mayor_material_list = cuerpo.cuerpomayormaterialdata_set.all()
    
    return render_to_response('cuerpo/mayor_material.html', {
                'cuerpo': cuerpo,
                'mayor_material_list': mayor_material_list,
                }, context_instance=RequestContext(request),
                )

# Show Mayor Material form
@authorize()
def edit_mayor_material_form(request, cuerpo, mayor_material_id):
    mayor_material_data = None
    # Attempt to load previously submitted data
    try:
        mayor_material_data = cuerpo.cuerpomayormaterialdata_set.get(pk=mayor_material_id)
    except CuerpoMayorMaterialData.DoesNotExist:
        # Redirect to default mayor material
        logging.error("Requested mayor material data id:%d for cuerpo:%d doesn't exists", mayor_material_id, cuerpo.id)
        request.flash['error'] = 'La planilla de material mayor consultada no existe'
        return redirect('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id)

    return generic_edit(request, mayor_material_data, CuerpoMayorMaterialForm, 'cuerpo/mayor_material_edit.html', reverse('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id), [[CuerpoMaterialMayorInstalledRadio, mayor_material_data], [CuerpoMaterialMayorPortableRadio, mayor_material_data], [CuerpoMaterialMayorAntenna, mayor_material_data]], ['company', cuerpo.company_set.all()])

# Add New Mayor Material form
@authorize()
def add_new_mayor_material(request, cuerpo):
    mayor_material_data = CuerpoMayorMaterialData()
    mayor_material_data.cuerpo = cuerpo
    
    return generic_edit(request, mayor_material_data, CuerpoMayorMaterialForm, 'cuerpo/mayor_material_edit.html', reverse('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id), [[CuerpoMaterialMayorInstalledRadio, mayor_material_data],[CuerpoMaterialMayorPortableRadio, mayor_material_data], [CuerpoMaterialMayorAntenna, mayor_material_data]], ['company', cuerpo.company_set.all()])
        

# Remove Selected Material form
@authorize()
def remove_mayor_material(request, cuerpo, mayor_material_id):
    if request.method == 'POST':
        mayor_material_data = None

        try:
            mayor_material_data = cuerpo.cuerpomayormaterialdata_set.get(pk=mayor_material_id)
        # The id provided in the url does not exist
        except CuerpoMayorMaterialData.DoesNotExist:
            # Redirect to default mayor material
            request.flash['error'] = 'La planilla de material mayor consultada no existe'
            logging.error("Requested mayor material data id:%d for cuerpo:%d doesn't exists", mayor_material_id, cuerpo.id)
            return redirect('cuerpo_mayor_material', cuerpo_id=cuerpo.old_id)
        
        logging.info("Deleting mayor material data object id:%d for cuerpo:%d", mayor_material_data.id, cuerpo.id)
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
    # If it fails, create blank data
    except ObjectDoesNotExist:
        alarm_central_cuerpo_data = CuerpoAlarmCentralData()
        # Add cuerpo to blank data
        alarm_central_cuerpo_data.cuerpo = cuerpo
        alarm_central_cuerpo_data.save()    


    #previene que se muestren los errores de envio al presionar el botón agregar otro
    prevent_validation_error = False

    AddBaseRadioEquipmentFormSet = inlineformset_factory(Cuerpo, CuerpoAlarmCentralBaseRadioEq, extra=0, can_delete=True)
    
    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST

        if 'add_new_base_radio_eq' in request.POST:
            
            # Get the data from POST
            new_base_radio_eq = AddBaseRadioEquipmentFormSet(prefix='base_radio', data=request.POST, instance=cuerpo)
            prevent_validation_error = True
            
            # Saving Added Rows
            for form in new_base_radio_eq.forms:
                if form.has_changed():
                    if form.is_valid():
                        form.save()
            ### Al usar sólo el request.POST para obtener y recargar los datos
            ### del formulario, los datos no tenían id de la base de datos (pues
            ### nunca eran cargados de ahí), luego al hacer cualquier modificación
            ### sobre éstos, eran considerados nuevos datos y se guardaban en la BD
            ### junto con la versión antigua (duplicación de líneas).
            ### Ahora estamos creando líneas vacías en la BD al hacer el agregar,
            ### para cargar de la base de datos. Toda línea que quede vacía después de
            ### llenar los datos debería eliminarse al hacer el guardado del formulario
            ### completo.
            
            # Create new empty line in DB
            cbre_new = CuerpoAlarmCentralBaseRadioEq(cuerpo=cuerpo, quantity=0, manufacturer=None, model='', power=0)
            cbre_new.save()
            
            # Reload data from DB
            new_base_radio_eq = AddBaseRadioEquipmentFormSet(prefix='base_radio',  instance=cuerpo)
        
        elif 'delete_base_radio_eq' in request.POST:
            prevent_validation_error = True
            new_base_radio_eq = AddBaseRadioEquipmentFormSet(prefix='base_radio', data=request.POST, instance=cuerpo)
            
            # Saving Changed Rows
            for form in new_base_radio_eq.forms:
                if form.is_valid():
                    if form.has_changed():
                        form.save()
                            
            # Then we delete the appropiate rows
            for form in new_base_radio_eq.deleted_forms:
                if form.is_valid():
                    coo_del = form.cleaned_data['id']
                    coo_del.delete()
                    
            new_base_radio_eq = AddBaseRadioEquipmentFormSet(prefix='base_radio', instance=cuerpo)
           
        else:
             # A form bound to the POST data
            form = CuerpoAlarmCentralForm(request.POST, instance=alarm_central_cuerpo_data)
            # If the form is correctly validated
            new_base_radio_eq = AddBaseRadioEquipmentFormSet(prefix='base_radio', data=request.POST, instance=cuerpo)
            if new_base_radio_eq.is_valid() and form.is_valid():      
                for fm in new_base_radio_eq.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            fm.save()
                form.save()
                ## Delete empty entries
                query = CuerpoAlarmCentralBaseRadioEq.objects.filter(cuerpo=cuerpo)
                for q in query:
                    if q.manufacturer == '' and q.model == '':
                        q.delete()
                # Redirect after POST
                return redirect('cuerpo_service_acts', cuerpo_id=cuerpo.old_id)
            # Else render the form again
            else:
                return render_to_response('cuerpo/alarm_central.html', {
                    'form': form,
                    'cuerpo': cuerpo,
                    'base_radio': new_base_radio_eq,
                    }, context_instance=RequestContext(request),
                    )
        # A form bound to the POST data
        form = CuerpoAlarmCentralForm(request.POST, instance=alarm_central_cuerpo_data)

    else:
        # If the form hasn't been submitted
        new_base_radio_eq = AddBaseRadioEquipmentFormSet(prefix='base_radio',instance=cuerpo)
    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoAlarmCentralForm(instance=alarm_central_cuerpo_data)

    # Render the form
    return render_to_response('cuerpo/alarm_central.html', {
            'form': form,
            'cuerpo': cuerpo,
            'base_radio': new_base_radio_eq,
            }, context_instance=RequestContext(request),
        )


# Show Service acts form
@authorize()
def display_service_acts_form(request, cuerpo):
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
            return redirect('index')
        # Else render the form again
        else:
            return render_to_response('cuerpo/service_acts.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoServiceActsForm(instance=service_acts_data)

    # Render the form
    return render_to_response('cuerpo/service_acts.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )
