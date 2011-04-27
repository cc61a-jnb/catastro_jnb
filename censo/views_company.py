# coding: utf-8

from utils import authorize

from censo.forms import CompanyPortadaPartialForm, CompanyVolunteerPartialForm
from censo.models import Company, VolunteerData
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

# Show main form
@authorize(roles=('company',))
def display_portada_form(request):
    profile = request.user.get_profile()
    # A profile must have a company asociated, this can't fail
    company = profile.company

    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CompanyPortadaPartialForm(request.POST, instance=company)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/company/volunteers')
        # Else render the form again
        else:
            return render_to_response('company/first_page.html', {
                'form': form,
                'company': company,
                }, context_instance=RequestContext(request),
                )
    # If the form hasn't been submitted
    
    # Load already submitted data as initial, to avoid triggering validation
    form = CompanyPortadaPartialForm(instance=company)

    # Render the form
    return render_to_response('company/first_page.html', {
            'form': form,
            'company': company,
            }, context_instance=RequestContext(request),
        )

# Show volunteer form
@authorize(roles=('company',))
def display_volunteers_form(request):
    profile = request.user.get_profile()
    company = profile.company
    volunteer_data = None
    # Attempt to load previously submitted data
    try:
        volunteer_data = company.volunteerdata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        volunteer_data = VolunteerData()
        # Add company to blank data
        volunteer_data.company = company
        volunteer_data.save()
    
    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CompanyVolunteerPartialForm(request.POST, instance=volunteer_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/company/infrastructure')
        # Else render the form again
        else:
            return render_to_response('company/second_page.html', {
                'form': form,
                'company': company,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted
    
    # Load already submitted data as initial, to avoid triggering validation
    form = CompanyVolunteerPartialForm(instance=volunteer_data)

    # Render the form
    return render_to_response('company/second_page.html', {
            'form': form,
            'company': company,
            }, context_instance=RequestContext(request),
        )

# Show infrastructure form (stub)
@authorize(roles=('company',))
def display_infrastructure_form(request):
    return render_to_response('company/third_page.html', {
            }, context_instance=RequestContext(request),
        )

# Show minor material form (stub)
@authorize(roles=('company',))
def display_minor_material_form(request):
    return render_to_response('company/fourth_page.html', {
            }, context_instance=RequestContext(request),
        )
