# coding: utf-8

from utils import authorize
from django.forms.models import inlineformset_factory
from censo.forms import CompanyPortadaForm, CompanyVolunteerForm, CompanyInfrastructureForm, CompanyMinorMaterialForm
from censo.models import Company, VolunteerData, InfrastructureCompanyData, MinorMaterialCompanyData, CompanyOtherOfficial
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
    
    prevent_validation_error = False
    AddOtherRoleCompanyFormSet = inlineformset_factory(Company, CompanyOtherOfficial, extra=0, can_delete=True)

    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST
        if 'add_other_official' in request.POST:
            cp = request.POST.copy()
            cp['other_official-TOTAL_FORMS'] = int(cp['other_official-TOTAL_FORMS']) + 1
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=cp, instance=company)
            prevent_validation_error = True
        elif 'delete_other_official' in request.POST:
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=request.POST, instance=company)
            
            for form in new_other_official.deleted_forms:
                if form.is_valid():
                    form.cleaned_data['id'].delete()    
                    
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', instance=company)
        else:
            # A form bound to the POST data
            form = CompanyPortadaForm(request.POST, instance=company)
            # If the form is correctly validated
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=request.POST, instance=company)
            if new_other_official.is_valid() and form.is_valid():
                new_other_official.save()
                form.save()
                # Redirect after POST
                return HttpResponseRedirect('/company/volunteers')
            # Else render the form again
            else:
                return render_to_response('company/first_page.html', {
                    'form': form,
                    'company': company,
                    'other_official': new_other_official,
                    }, context_instance=RequestContext(request),
                    )
    else:
        # If the form hasn't been submitted
        new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official',instance=company)
    
    # Load already submitted data as initial, to avoid triggering validation
    form = CompanyPortadaForm(instance=company)

    # Render the form
    return render_to_response('company/first_page.html', {
            'form': form,
            'company': company,
            'other_official': new_other_official,
            'prevent_validation_error': prevent_validation_error,
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
        form = CompanyVolunteerForm(request.POST, instance=volunteer_data)
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
    form = CompanyVolunteerForm(instance=volunteer_data)

    # Render the form
    return render_to_response('company/second_page.html', {
            'form': form,
            'company': company,
            }, context_instance=RequestContext(request),
        )

# Show infrastructure form (stub)
@authorize(roles=('company',))
def display_infrastructure_form(request):
    profile = request.user.get_profile()
    company = profile.company
    infrastructure_company_data = None
    # Attempt to load previously submitted data
    try:
        infrastructure_company_data = company.infrastructurecompanydata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        infrastructure_company_data = InfrastructureCompanyData()
        # Add company to blank data
        infrastructure_company_data.company = company
        infrastructure_company_data.save()
    
    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CompanyInfrastructureForm(request.POST, instance=infrastructure_company_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/company/minor_material')
        # Else render the form again
        else:
            return render_to_response('company/third_page.html', {
                'form': form,
                'company': company,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted
    
    # Load already submitted data as initial, to avoid triggering validation
    form = CompanyInfrastructureForm(instance=infrastructure_company_data)

    # Render the form
    return render_to_response('company/third_page.html', {
            'form': form,
            'company': company,
            }, context_instance=RequestContext(request),
        )


# Show minor material form (stub)
@authorize(roles=('company',))
def display_minor_material_form(request):
    profile = request.user.get_profile()
    company = profile.company
    minor_material_company_data = None
    # Attempt to load previously submitted data
    try:
        minor_material_company_data = company.minormaterialcompanydata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        minor_material_company_data = MinorMaterialCompanyData()
        # Add company to blank data
        minor_material_company_data.company = company
        minor_material_company_data.save()
    
    # If the form has been submitted
    if request.method == 'POST':
        # A form bound to the POST data
        form = CompanyMinorMaterialForm(request.POST, instance=minor_material_company_data)
        # If the form is correctly validated
        if form.is_valid():
            form.save()
            # Redirect after POST
            return HttpResponseRedirect('/company/')
        # Else render the form again
        else:
            return render_to_response('company/fourth_page.html', {
                'form': form,
                'company': company,
                }, context_instance=RequestContext(request),
                )

    # If the form hasn't been submitted
    
    # Load already submitted data as initial, to avoid triggering validation
    form = CompanyMinorMaterialForm(instance=minor_material_company_data)

    # Render the form    
    return render_to_response('company/fourth_page.html', {
                'form': form,
                'company': company,
            }, context_instance=RequestContext(request),
        )
