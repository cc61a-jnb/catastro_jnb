# coding: utf-8

from utils import generic_edit
from authentication import authorize

from censo.forms import *
from censo.models import *

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Show main form
@authorize(roles=('company',))
def display_portada_form(request):
    profile = request.user.get_profile()
    # A profile must have a company asociated, this can't fail
    company = profile.company
    # Attempt to load previously submitted data
    try:
        portada_data = company.portadacompanydata
        # If it fails, create blank data
    except ObjectDoesNotExist:
        portada_data = PortadaCompanyData()
        # Add company to blank data
        portada_data.company = company
        portada_data.save() 
        
    return generic_edit(request, portada_data, CompanyPortadaForm, 'company/first_page.html', reverse('catastro_jnb.censo.views_company.display_volunteers_form'), [[CompanyOtherOfficial, company]])

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
    
    return generic_edit(request, volunteer_data, CompanyVolunteerForm, 'company/second_page.html', reverse('catastro_jnb.censo.views_company.display_infrastructure_form'))
    
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
    return generic_edit(request, infrastructure_company_data, CompanyInfrastructureForm, 'company/third_page.html', reverse('catastro_jnb.censo.views_company.display_minor_material_form'))

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
    #call to generic function to show dynamic fields    
    return generic_edit(request, minor_material_company_data, CompanyMinorMaterialForm, 'company/fourth_page.html', reverse('catastro_jnb.censo.views_company.display_portada_form'), [[CompanyOtherRadioBase, company], [CompanyOtherRadioPortable, company]])
