# coding: utf-8

from utils import authorize
from censo.forms import *
from censo.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from utils import generic_edit
import ipdb

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
        
        z = dict(request.POST, **request.FILES)
        form = CompanyInfrastructureForm(request.POST, request.FILES, instance=infrastructure_company_data)
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

    prevent_validation_error = False
    AddOtherBaseRadioCompanyFormSet = inlineformset_factory(Company, CompanyOtherRadioBase, extra=0, can_delete=True)
    AddOtherPortableRadioCompanyFormSet = inlineformset_factory(Company, CompanyOtherRadioPortable, extra=0, can_delete=True)
    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST
        main_form = CompanyMinorMaterialForm(request.POST, instance=minor_material_company_data)
        
        #Add Radio Base
        if 'add_radio_base' in request.POST:
            new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio', data=request.POST, instance=company)
            prevent_validation_error = True

            for form in new_other_base_radio.forms:
                if form.has_changed():
                    if form.is_valid():
                        form.save()
            # Create new empty line in DB
            create_new_other_radio_base = CompanyOtherRadioBase(company=company, radio_brand='', radio_model='')
            create_new_other_radio_base.save()

            # Reload data from DB
            new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio',  instance=company)

            if main_form.is_valid():
                main_form.save()
                
         #Add Radio Portatil
        elif 'add_radio_portatil' in request.POST:
            new_other_portable_radio = AddOtherPortableRadioCompanyFormSet(prefix='other_portable_radio', data=request.POST, instance=company)
            prevent_validation_error = True

            for form in new_other_portable_radio.forms:
                if form.has_changed():
                    if form.is_valid():
                        form.save()
            # Create new empty line in DB
            create_new_other_radio_base = CompanyOtherRadioPortable(company=company, radio_portable_brand='', radio_portable_model='', radio_portable_power=0)
            create_new_other_radio_base.save()

            # Reload data from DB
            new_other_base_radio = AddOtherPortableRadioCompanyFormSet(prefix='other_portable_radio',  instance=company)

            if main_form.is_valid():
                main_form.save()   

        #Delete Radio Portatil
        elif 'delete_radio_portable' in request.POST:
            prevent_validation_error = True
            new_portable_radio = AddOtherPortableRadioCompanyFormSet(prefix='delete_radio_portable', data=request.POST, instance=company)

            # Saving Changed Rows
            for form in new_portable_radio.forms:
                if form.is_valid():
                    if form.has_changed():
                        form.save()

           # Then we delete the appropiate rows
            for form in new_portable_radio.deleted_forms:
                if form.is_valid():
                    coo_del = form.cleaned_data['id']
                    coo_del.delete()

            new_portable_radio = AddOtherPortableRadioCompanyFormSet(prefix='delete_radio_portable', instance=company)
            # If the form is correctly validated
            if main_form.is_valid():
                main_form.save()
        
        #Delete Radio Base        
        elif 'delete_other_radio_base' in request.POST:
            prevent_validation_error = True
            new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio', data=request.POST, instance=company)

            # Saving Changed Rows
            for form in new_other_base_radio.forms:
                if form.is_valid():
                    if form.has_changed():
                        form.save()

           # Then we delete the appropiate rows
            for form in new_other_base_radio.deleted_forms:
                if form.is_valid():
                    coo_del = form.cleaned_data['id']
                    coo_del.delete()

            new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio', instance=company)
            # If the form is correctly validated
            if main_form.is_valid():
                main_form.save()
        
        #Other cases
        else:
            # A form bound to the POST data
            main_form = CompanyMinorMaterialForm(request.POST, instance=portada_data)
            # If the form is correctly validated
            new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio', data=request.POST, instance=company)
            
            if new_other_base_radio.is_valid() and main_form.is_valid():
                for fm in new_other_base_radio.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            fm.save()
                main_form.save()
                
            new_other_portable_radio = AddOtherPortableRadioCompanyFormSet(prefix='delete_radio_portable', instance=company)
            
            if new_other_portable_radio.is_valid() and main_form.is_valid():
                for fm in new_other_portable_radio.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            fm.save()
                main_form.save()

                ## Delete empty entries
                query = CompanyOtherRadioBase.objects.filter(company=company)
                for q in query:
                    if q.radio_brand == '' and q.radio_model == '':
                        q.delete()
                        
                ## Delete empty entries
                query = CompanyOtherRadioPortable.objects.filter(company=company)
                for q in query:
                    if q.radio_portable_brand == '' and q.radio_portable_model == '':
                        q.delete()
                # Redirect after POST
                return HttpResponseRedirect('/company/')
            # Else render the form again
            else:
                return render_to_response('company/fourth_page.html', {
                    'form': main_form,
                    'others_radio_base': new_other_base_radio,
                    'others_radio_portable': new_other_portable_radio,
                    'company': company,
                    }, context_instance=RequestContext(request),
                    )


        # A form bound to the POST data
        main_form = CompanyMinorMaterialForm(request.POST, instance=company)
    else:
        # If the form hasn't been submitted
        new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio',instance=company)
    new_other_portable_radio = AddOtherPortableRadioCompanyFormSet(prefix='other_portable_radio',instance=company)
    # Load already submitted data as initial, to avoid triggering validation
    main_form = CompanyMinorMaterialForm(instance=minor_material_company_data)

    # Render the form
    return render_to_response('company/fourth_page.html', {
                'form': main_form,
                'others_radio_base': new_other_base_radio,
                'others_radio_portable': new_other_portable_radio,
                'prevent_validation_error': prevent_validation_error,
                'company': company,
            }, context_instance=RequestContext(request),
        )
