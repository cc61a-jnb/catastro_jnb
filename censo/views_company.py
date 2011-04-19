# coding: utf-8

from censo.forms import CompanyPortadaForm
from censo.forms import CompanyVolunteerPartialForm
from censo.forms import CompanyVolunteerForm
from censo.models import Company
from censo.models import VolunteerData

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.core.exceptions import ObjectDoesNotExist


def company_login_required(f):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated():
            request.flash['notice'] = 'Por favor inicie sesión primero'
            return HttpResponseRedirect('/login')
            
        role = request.user.get_profile().latest_role()
        if not role:
            request.flash['error'] = 'Usted no tiene roles asociados'
        elif role.old_id in [1, 2]:
            return HttpResponseRedirect('/cuerpo/')
        elif role.old_id in [4]:
            return f(request, *args, **kwargs)
        else:
            request.flash['error'] = 'Usted no tiene permisos para acceder al sistema'
    
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

@company_login_required
def display_portada_form(request):
    profile = request.user.get_profile()
    company = profile.company
    initial_data = {
        'address': company.address,
        'phone': company.phone,
        'foundation_date': company.foundation_date,
    }

    if request.method == 'POST': # If the form has been submitted...
        form = CompanyPortadaForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            company.address = form.cleaned_data['address']
            company.phone = form.cleaned_data['phone']
            company.foundation_date = form.cleaned_data['foundation_date']
            company.save()
            return HttpResponseRedirect('/company/volunteers') # Redirect after POST
        else:
            return render_to_response('company/first_page.html', {
                'form': form,
                }, context_instance=RequestContext(request),
                )
    
    form = CompanyPortadaForm(initial=initial_data) # si no lo pasamos como intitial, se activa la validacion

    return render_to_response('company/first_page.html', {
            'form': form,
            'company': company,
            }, context_instance=RequestContext(request),
        )

@company_login_required
def display_volunteers_form(request):
    profile = request.user.get_profile()
    company = profile.company
    volunteer_data = None
    try:
        volunteer_data = company.volunteerdata
    except ObjectDoesNotExist:
        volunteer_data = VolunteerData()
        volunteer_data.company = company
        volunteer_data.save()

    if request.method == 'POST': # If the form has been submitted...
        form = CompanyVolunteerPartialForm(request.POST, instance=volunteer_data) # A form bound to the POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/company/infrastructure') # Redirect after POST
        else:
            return render_to_response('company/second_page.html', {
                'form': form,
                }, context_instance=RequestContext(request),
                )

    form = CompanyVolunteerPartialForm(instance=volunteer_data) # si no lo pasamos como intitial, se activa la validacion

    return render_to_response('company/second_page.html', {
            'form': form,
            'company': company,
            }, context_instance=RequestContext(request),
        )

@company_login_required
def display_infrastructure_form(request):
    return render_to_response('company/third_page.html', {
            }, context_instance=RequestContext(request),
        )

@company_login_required
def display_minor_material_form(request):
    return render_to_response('company/fourth_page.html', {
            }, context_instance=RequestContext(request),
        )