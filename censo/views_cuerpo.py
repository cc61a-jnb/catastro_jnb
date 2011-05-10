# coding: utf-8

from utils import authorize

from censo.forms import *
from censo.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import inlineformset_factory


# Show main form
@authorize(roles=('cuerpo',))
def display_portada_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    #previene que se muestren los errores de envio al presionar el botón agregar otro
    prevent_validation_error = False

    AddOtherRoleCuerpoFormSet = inlineformset_factory(Cuerpo, CuerpoOtherOfficial, extra=0, can_delete=True)
    # companies = cuerpo
    # TODO: add company selector

    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST

        if 'add_other_official' in request.POST:
            cp = request.POST.copy()
            cp['other_official-TOTAL_FORMS'] = int(cp['other_official-TOTAL_FORMS']) + 1
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', data=cp, instance=cuerpo)
            prevent_validation_error = True
            # We use the POST data to add anything new
            for form in new_other_official.forms:
                if form.has_changed():
                    if form.is_valid():
                        coo_query = CuerpoOtherOfficial.objects.filter(cuerpo=cuerpo, role_name=form.cleaned_data['role_name'], person_name=form.cleaned_data['person_name'])
                        if not coo_query:
                            form.save()
        elif 'delete_other_official' in request.POST:
            ## Delete from DB
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', data=request.POST, instance=cuerpo)
            for form in new_other_official.deleted_forms:
                if form.is_valid():
                    coo_query = CuerpoOtherOfficial.objects.filter(cuerpo=cuerpo, role_name=form.cleaned_data['role_name'], person_name=form.cleaned_data['person_name'])
                    if coo_query:
                        coo_query[0].delete()
            ## Check and delete null entries
            query = CuerpoOtherOfficial.objects.all()
            for q in query:
                if q.role_name == None and q.person_name == None:
                    q.delete()
            ## Regenerate formset without deleted rows
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', instance=cuerpo)
        else:
             # A form bound to the POST data
            form = CuerpoPortadaForm(request.POST, instance=cuerpo)
            # If the form is correctly validated
            new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official', data=request.POST, instance=cuerpo)
            if new_other_official.is_valid() and form.is_valid():      
                for fm in new_other_official.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            coo_query = CuerpoOtherOfficial.objects.filter(cuerpo=cuerpo, role_name=fm.cleaned_data['role_name'], person_name=fm.cleaned_data['person_name'])
                            if not coo_query:
                                fm.save()
                form.save()
                ## Delete null entries
                query = CuerpoOtherOfficial.objects.all()
                for q in query:
                    if q.role_name == None and q.person_name == None:
                        q.delete()
                # Redirect after POST
                return HttpResponseRedirect('/cuerpo/general')
            # Else render the form again
            else:
                return render_to_response('cuerpo/first_page.html', {
                    'form': form,
                    'cuerpo': cuerpo,
                    'other_official': new_other_official,
                    }, context_instance=RequestContext(request),
                    )
        # A form bound to the POST data
        form = CuerpoPortadaForm(request.POST, instance=cuerpo)

    else:
        # If the form hasn't been submitted
        new_other_official = AddOtherRoleCuerpoFormSet(prefix='other_official',instance=cuerpo)
    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoPortadaForm(instance=cuerpo)

    # Render the form
    return render_to_response('cuerpo/first_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            'other_official': new_other_official,
            }, context_instance=RequestContext(request),
        )

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
            return HttpResponseRedirect('/cuerpo/anb')
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

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        z = dict(request.POST, **request.FILES)
        form = CuerpoInfrastructureForm(request.POST, request.FILES, instance=infrastructure_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/cuerpo/infrastructure')
        # Else render the form again
        else:
            return render_to_response('cuerpo/fourth_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoInfrastructureForm(instance=infrastructure_data)

    # Render the form
    return render_to_response('cuerpo/fourth_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

# Show Mayor Material form
@authorize(roles=('cuerpo',))
def display_mayor_material_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    mayor_material_data = None
    # Attempt to load previously submitted data
    try:
        mayor_material_data = cuerpo.cuerpomayormaterialdata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        mayor_material_data = CuerpoMayorMaterialData()
        # Add cuerpo to blank data
        mayor_material_data.cuerpo = cuerpo
        mayor_material_data.save()

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CuerpoMayorMaterialForm(request.POST, instance=mayor_material_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/cuerpo/mayormaterial')
        # Else render the form again
        else:
            return render_to_response('cuerpo/fifth_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoMayorMaterialForm(instance=mayor_material_data)

    # Render the form
    return render_to_response('cuerpo/fifth_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

# Show Alarm Central form
@authorize(roles=('cuerpo',))
def display_alarm_central_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    alarm_central_data = None
    # Attempt to load previously submitted data
    try:
        alarm_central_data = cuerpo.cuerpoalarmcentraldata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        alarm_central_data = CuerpoAlarmCentralData()
        # Add cuerpo to blank data
        alarm_central_data.cuerpo = cuerpo
        alarm_central_data.save()

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CuerpoAlarmCentralForm(request.POST, instance=alarm_central_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/cuerpo/alarmcentral')
        # Else render the form again
        else:
            return render_to_response('cuerpo/sixth_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted

    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoAlarmCentralForm(instance=alarm_central_data)

    # Render the form
    return render_to_response('cuerpo/sixth_page.html', {
            'form': form,
            'cuerpo': cuerpo,
            }, context_instance=RequestContext(request),
        )

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
