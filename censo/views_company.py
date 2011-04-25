# coding: utf-8

from censo.forms import CompanyPortadaPartialForm, CompanyVolunteerPartialForm
from censo.models import Company, VolunteerData
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

# Check if user's role can access company form
def company_login_required(f):
    def wrap(request, *args, **kwargs):
        # If user isn't authenticated
        if not request.user.is_authenticated():
            request.flash['notice'] = 'Por favor inicie sesión primero'
            return HttpResponseRedirect('/login')
        
        # Get user role    
        role = request.user.get_profile().latest_role()
        # If user doesn't have roles, error
        if not role:
            request.flash['error'] = 'Usted no tiene roles asociados'
        # If user's role has access to /cuerpo/, redirect
        elif role.old_id in [1, 2]:
            return HttpResponseRedirect('/cuerpo/')
        # If user's role has access to /company/, validate and grant access
        elif role.old_id in [4]:
            return f(request, *args, **kwargs)
        # If user's role doesn't have access, error
        else:
            request.flash['error'] = 'Usted no tiene permisos para acceder al sistema'
    
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

# Show main form
@company_login_required
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
@company_login_required
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
@company_login_required
def display_infrastructure_form(request):
    return render_to_response('company/third_page.html', {
            }, context_instance=RequestContext(request),
        )

# Show minor material form (stub)
@company_login_required
def display_minor_material_form(request):
    return render_to_response('company/fourth_page.html', {
            }, context_instance=RequestContext(request),
        )
