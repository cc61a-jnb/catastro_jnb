# coding: utf-8

from utils import authorize
from django.forms.models import inlineformset_factory
from censo.forms import *
from censo.models import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
import re
import ipdb

def remove_deleted_fields_from_data(data, prefix):
    total_forms = int(data['%s-TOTAL_FORMS' % prefix])
    
    return_data = {}
    insertion_index = 0
    new_initial_count = 0
    
    for i in range(total_forms):
        base_pattern = '%s-%d' % (prefix, i)
        if '%s-DELETE' % base_pattern not in data:
            for key, value in data.items():
                if base_pattern in key:
                    new_key = re.sub(r'^(%s-)\d+(-.+)$' % prefix, r'\1%d\2', key) % insertion_index
                    return_data[new_key] = value
                    if key == '%s-id' % base_pattern and value:
                        new_initial_count += 1
            insertion_index += 1
                        
    return_data['%s-TOTAL_FORMS' % prefix] = insertion_index
    return_data['%s-MAX_NUM_FORMS' % prefix] = data['%s-MAX_NUM_FORMS' % prefix]
    return_data['%s-INITIAL_FORMS' % prefix] = new_initial_count
    return return_data

def find_foreign_key_field_name(ReferralClass, ReferredClass):
    for field in ReferralClass._meta._fields():
        if hasattr(field, 'related') and field.related.parent_model == ReferredClass:
            return field.name

def _generic_edit(base_instance, instance, request, ReferredForm, ReferredClass, Referral, template, success_redirect):
    GenericFormSet = inlineformset_factory(ReferredClass, Referral, extra=0)
    prevent_validation_errors = False
    prefix = GenericFormSet.get_default_prefix()

    if request.method == 'POST':
        form = ReferredForm(request.POST, instance=instance)
        if '%s_add' % prefix in request.POST:
            formset_data = request.POST.copy()
            total_forms_field_name = '%s-TOTAL_FORMS' % prefix
            total_forms_quantity = int(formset_data[total_forms_field_name])
            formset_data[total_forms_field_name] = str(total_forms_quantity + 1)
            
            formset = GenericFormSet(formset_data, instance=base_instance)
            prevent_validation_errors = True
        elif '%s_delete' % prefix in request.POST:
            new_data = remove_deleted_fields_from_data(request.POST, prefix)
            formset = GenericFormSet(new_data, instance=base_instance)
            prevent_validation_errors = True
        else:
            formset = GenericFormSet(request.POST, instance=base_instance)
            if form.is_valid() and formset.is_valid():
                form.save()
                
                foreign_key_field_name = find_foreign_key_field_name(Referral, ReferredClass)
                
                for f in formset.forms:
                    if f.has_changed():
                        setattr(f.instance, foreign_key_field_name, base_instance)
                        f.instance.save()
                        
                commit_ids = [f.instance.id for f in formset.forms if f.instance.id]
                
                if instance:
                    for referral_object in formset.queryset:
                        if referral_object.id not in commit_ids:
                            referral_object.delete()
                    
                return HttpResponseRedirect(success_redirect)
    else:
        formset = GenericFormSet(instance=base_instance)
        form = ReferredForm(instance=instance)
        
    return render_to_response(template, {
            'form': form,
            'formset': formset,
            'prefix': prefix,
            'base_instance': base_instance,
            }, context_instance=RequestContext(request),
        )

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
        
    return _generic_edit(company, portada_data, request, CompanyPortadaForm, Company, CompanyOtherOfficial, 'company/first_page.html', reverse('catastro_jnb.censo.views_company.display_volunteers_form'))

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
    prevent_validation_error = False
    #pdb.set_trace()
    # Attempt to load previously submitted data
    try:
        minor_material_company_data = company.minormaterialcompanydata
    # If it fails, create blank data
    except ObjectDoesNotExist:
        minor_material_company_data = MinorMaterialCompanyData()
        # Add company to blank data
        minor_material_company_data.company = company
        minor_material_company_data.save()


    AddOtherBaseRadioCompanyFormSet = inlineformset_factory(Company, CompanyOtherRadioBase, extra=0, can_delete=True)
    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST
        # A form bound to the POST data
        main_form = CompanyMinorMaterialForm(request.POST, instance=minor_material_company_data)
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
        else:
        # A form bound to the POST data
         main_form = CompanyMinorMaterialForm(request.POST, instance=portada_data)
        # If the form is correctly validated
         new_other_official = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio', data=request.POST, instance=company)
         if new_other_base_radio.is_valid() and main_form.is_valid():
                for fm in new_other_base_radio.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            fm.save()
                main_form.save()

                ## Delete empty entries
                query = CompanyOtherRadioBase.objects.filter(company=company)
                for q in query:
                    if q.radio_brand == '' and q.radio_model == '':
                        q.delete()
            # Redirect after POST
                return HttpResponseRedirect('/company/')
        # Else render the form again
         else:
            return render_to_response('company/fourth_page.html', {
                'form': main_form,
                'others_radio_base': new_other_radio_base,
                'company': company,
                }, context_instance=RequestContext(request),
                )


        # A form bound to the POST data
            main_form = CompanyMinorMaterialForm(request.POST, instance=company)
    else:
        # If the form hasn't been submitted
        new_other_base_radio = AddOtherBaseRadioCompanyFormSet(prefix='other_base_radio',instance=company)
    # Load already submitted data as initial, to avoid triggering validation
    main_form = CompanyMinorMaterialForm(instance=minor_material_company_data)

    # Render the form
    return render_to_response('company/fourth_page.html', {
                'form': main_form,
                'others_radio_base': new_other_base_radio,
                'prevent_validation_error': prevent_validation_error,
                'company': company,
            }, context_instance=RequestContext(request),
        )
