# coding: utf-8

import logging

from utils import generic_edit
from authentication import authorize

from censo.forms import *
from censo.models import *

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Show main form
@authorize()
def display_portada_form(request, company):
    # Attempt to load previously submitted data
    try:
        portada_data = company.portadacompanydata
        logging.info("Successfully fetched company:%s's portadacompanydata for user:%s", company.old_id, request.user.username)
        # If it fails, create blank data
    except ObjectDoesNotExist:
        portada_data = PortadaCompanyData()
        logging.info("Creating company:%s's portadacompanydata model for user:%s", company.old_id, request.user.username)
        # Add company to blank data
        portada_data.company = company
        portada_data.save() 
    
	#Dynamic input fields    
    return generic_edit(request, portada_data, CompanyPortadaForm, 'company/portada.html', reverse('company_volunteers', kwargs={'company_id':company.old_id}), [[CompanyOtherOfficial, company]])

# Show volunteer form
@authorize()
def display_volunteers_form(request, company):
    volunteer_data = None
    # Attempt to load previously submitted data
    try:
        volunteer_data = company.volunteerdata
        logging.info("Successfully fetched company:%s's volunteerdata for user:%s", company.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating company:%s's volunteerdata model for user:%s", company.old_id, request.user.username)
        volunteer_data = VolunteerData()
        # Add company to blank data
        volunteer_data.company = company
        volunteer_data.save()
		
    #Dynamic input fields
    return generic_edit(request, volunteer_data, CompanyVolunteerForm, 'company/volunteers.html', reverse('company_infrastructure', kwargs={'company_id':company.old_id}))
    
# Show infrastructure form (stub)
@authorize()
def display_infrastructure_form(request, company):
    infrastructure_company_data = None
    # Attempt to load previously submitted data
    try:
        infrastructure_company_data = company.infrastructurecompanydata
        logging.info("Successfully fetched company:%s's infrastructurecompanydata for user:%s", company.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating company:%s's infrastructurecompanydata model for user%s", company.old_id, request.user.username)
        infrastructure_company_data = InfrastructureCompanyData()
        # Add company to blank data
        infrastructure_company_data.company = company
        infrastructure_company_data.save()

    return generic_edit(request, infrastructure_company_data, CompanyInfrastructureForm, 'company/infrastructure.html', reverse('company_minor_material', kwargs={'company_id':company.old_id}), [[CompanyElectGeneratorFixedBarracks, infrastructure_company_data]])

# Show minor material form (stub)
@authorize()
def display_minor_material_form(request, company):
    minor_material_company_data = None
    
    # Attempt to load previously submitted data
    try:
        minor_material_company_data = company.minormaterialcompanydata
        logging.info("Successfully fetched company:%s's minormaterialcompanydata for user:%s", company.old_id, request.user.username)
    # If it fails, create blank data
    except ObjectDoesNotExist:
        logging.info("Creating company:%s's minormaterialcompanydata model for user:%s", company.old_id, request.user.username)
        minor_material_company_data = MinorMaterialCompanyData()
        # Add company to blank data
        minor_material_company_data.company = company
        minor_material_company_data.save()
		
    #call to generic function to show dynamic fields    
    return generic_edit(request, minor_material_company_data, CompanyMinorMaterialForm, 'company/minor_material.html', reverse('company', kwargs={'company_id':company.old_id}), [[CompanyOtherRadioBase, company], [CompanyOtherRadioPortable, company],[CompanyAntenas, company]])
