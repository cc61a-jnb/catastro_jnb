# coding: utf-8

import logging

from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response
import re
import pdb

def render_service_acts(fields, column_labels, row_labels, css_class_name='table_service_acts'):
    template = loader.get_template('tags/fields_table_service_acts.html')

    #helper text array
    helper_text = []
    single_fields = []
    for row_field in fields:
        single_fields.extend(row_field)

    for index, item in enumerate(fields):
        helper_text.append(item[0].help_text)
    errors = combine_fields_errors(single_fields)

    for idx, row_fields in enumerate(fields):
        row_fields.insert(0, "<b>%s</b> <p class='nota'>%s</p>" % (row_labels[idx], helper_text[idx]) )

    c = Context({
        'helper_text': helper_text,
        'fields': fields,
        'errors': errors,
        'column_labels': column_labels,
        'css_class_name': css_class_name,
    })
    return template.render(c)

def render_fields_as_table(fields, column_labels, row_labels, css_class_name='table_service_acts'):
    template = loader.get_template('tags/fields_table.html')

    #helper text array
    helper_text = []
    single_fields = []
    for row_field in fields:
        single_fields.extend(row_field)

    for index, item in enumerate(fields):
        helper_text.append(item[0].help_text)
    errors = combine_fields_errors(single_fields)

    for idx, row_fields in enumerate(fields):
        row_fields.insert(0, "%s <br><small>%s</small>" % (row_labels[idx], helper_text[idx]) )

    c = Context({
        'helper_text': helper_text,
        'fields': fields,
        'errors': errors,
        'column_labels': column_labels,
        'css_class_name': css_class_name,
    })
    return template.render(c)

def render_fields_as_list(fields, css_class_name='list_fields'):
    template = loader.get_template('tags/fields_list.html')
    errors = combine_fields_errors(fields)

    c = Context({
        'fields': fields,
        'errors': errors,
        'css_class_name': css_class_name,
    })

    return template.render(c)

def combine_fields_errors(fields):
    '''
Method that combines the errors from multiple fields in
a single array.
'''
    errors = []
    for field in fields:
        errors.extend(field.errors)
    return errors

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

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

def generic_edit(request, instance, PageForm, template, success_redirect, formset_pairs=[], queryset_pair=[]):
    '''
    Method that handles form with multiple (or no) formsets automagically
    request: Request sent to the original view
    instance: data associated with the current page
    e.g. an instance of PortadaCompanyData
    PageForm: Class of the form associated with the page
    e.g. CompanyPortadaForm
    template: The template that renders this page
    e.g. company/first_page.html
    success_redirect: The URL of the page to redirect to if this form and its subforms are valid
    e.g. /company/volunteers
    formset_pairs: Optional list of pairs for the data needed to analyze each formset, the first
    one must be the model class that represents the formset (e.g CompanyOtherOfficial), the second
    one must be the instance of the model the class refers to (e.g. company)
    '''
    
    # First we generate all the formset classes with the given formset_pairs
    GenericFormSets = [inlineformset_factory(pair[1].__class__, pair[0], extra=1) for pair in formset_pairs]
    
    # Flag that is set to true if something "happened" to one of the formsets (added or deleted)
    # sent to the template if we want to, for example, to prevent the showing of validation errors
    # on the main form
    formsets_modified = False
    formset_error=None
    
    # Dictionary that holds the formsets after adding, deleting and validating them
    # Key is the default prefix of the class
    formsets = {}
    # If one of the buttons has been pressed
    
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=instance)
        
        for picture_field in form.picture_fields():
            picture_name = picture_field[0].name
            if '%s_delete' % picture_name in request.POST:
                getattr(instance, picture_name).delete()
                formsets_modified = True
        
        for idx, GenericFormSet in enumerate(GenericFormSets):
            prefix = GenericFormSet.get_default_prefix()
            
            if '%s_add' % prefix in request.POST:
                formset_data = request.POST.copy()
                total_forms_field_name = '%s-TOTAL_FORMS' % prefix
                total_forms_quantity = int(formset_data[total_forms_field_name])
                formset_data[total_forms_field_name] = str(total_forms_quantity + 1)
                
                formsets[prefix] = GenericFormSet(formset_data, instance=formset_pairs[idx][1])
                formsets_modified = True
                break
            elif '%s_delete' % prefix in request.POST:
                new_data = remove_deleted_fields_from_data(request.POST, prefix)
                formsets[prefix] = GenericFormSet(new_data, instance=formset_pairs[idx][1])
                formsets_modified = True
                break
        if formsets:
            for idx, GenericFormSet in enumerate(GenericFormSets):
                prefix = GenericFormSet.get_default_prefix()
                if prefix not in formsets:
                    formsets[prefix] = GenericFormSet(request.POST, instance=formset_pairs[idx][1])
        else:
            valid_form_page = form.is_valid()
            
            for idx, GenericFormSet in enumerate(GenericFormSets):
                formset = GenericFormSet(request.POST, instance=formset_pairs[idx][1])
                if not formset.is_valid():
                    valid_form_page = False
                    formset_error=u'Por favor corrija los errores en la ficha'
                formsets[GenericFormSet.get_default_prefix()] = formset
 
            if valid_form_page and not formsets_modified:
                form.save()
                
                for idx, GenericFormSet in enumerate(GenericFormSets):
                    prefix = GenericFormSet.get_default_prefix()
                    formset = formsets[prefix]
                
                    foreign_key_field_name = find_foreign_key_field_name(formset_pairs[idx][0], formset_pairs[idx][1].__class__)
                    
                    for f in formset.forms:
                        if f.has_changed():
                            setattr(f.instance, foreign_key_field_name, formset_pairs[idx][1])
                            f.instance.save()
                            
                    commit_ids = [f.instance.id for f in formset.forms if f.instance.id]
                    
                    for referral_object in formset.queryset:
                        if referral_object.id not in commit_ids:
                            referral_object.delete()
                    
                return HttpResponseRedirect(success_redirect)
    else:
        for idx, GenericFormSet in enumerate(GenericFormSets):
            prefix = GenericFormSet.get_default_prefix()
            formsets[prefix] = GenericFormSet(instance=formset_pairs[idx][1])
        form = PageForm(instance=instance)
        
    if queryset_pair:
        form.fields[queryset_pair[0]].queryset = queryset_pair[1]
        
    menu_titles, main_menu_choices, user_permission_instance = request.user.get_profile().get_menu()
        
    return render_to_response(template, {
            'form': form,
            'formsets': formsets,
            'formset_error': formset_error,
            'instance': instance,
            'user_permission_instance': user_permission_instance,
            'formsets_modified': formsets_modified,
            'menu_titles': menu_titles,
            'real_menu_titles': menu_titles[:-1],
            'main_menu_choices': main_menu_choices,
            }, context_instance=RequestContext(request),
        )
        
def get_menu_titles(Class):
    if not Class:
        return []
    else:
        titles = [Class.menu_pack()]
        titles.extend(get_menu_titles(Class.hierarchical_child()))
        return titles
        
def get_menu_data(instance):
    if not instance:
        return [[], None, False]
        
    choices = instance.referring_children()
    titles = get_menu_titles(instance.hierarchical_child())
    
    return [titles, choices, instance]
