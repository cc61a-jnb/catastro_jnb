# coding: utf-8

from utils import authorize

from censo.forms import CuerpoPortadaForm, CuerpoGeneralForm, CuerpoANBForm, CuerpoInfrastructureForm
from censo.models import Cuerpo, Company, CuerpoGeneralData, CuerpoANBData, CuerpoInfrastructureData
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

# Show main form
@authorize(roles=('cuerpo',))
def display_portada_form(request):
    profile = request.user.get_profile()
    cuerpo = profile.company.cuerpo
    # companies = cuerpo
    # TODO: add company selector

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CuerpoPortadaForm(request.POST, instance=cuerpo)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/cuerpo/general')
        # Else render the form again
        else:
            return render_to_response('cuerpo/first_page.html', {
                'form': form,
                'cuerpo': cuerpo,
                }, context_instance=RequestContext(request),
                )
    # If the form hasn't been submitted
    
    # Load already submitted data as initial, to avoid triggering validation
    form = CuerpoPortadaForm(instance=cuerpo)

    # Render the form
    return render_to_response('cuerpo/first_page.html', {
            'form': form,
            'cuerpo': cuerpo,
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
        form = CuerpoInfrastructureForm(request.POST, instance=infrastructure_data)
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
