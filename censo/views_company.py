# coding: utf-8

from utils import authorize
from django.forms.models import inlineformset_factory
from censo.forms import *
from censo.models import *
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
    
    #previene que se muestren los errores de envio al presionar el botón agregar otro
    prevent_validation_error = False
    
    AddOtherRoleCompanyFormSet = inlineformset_factory(Company, CompanyOtherOfficial, extra=0, can_delete=True)

    # If the form has been submitted
    if request.method == 'POST':
        args = request.POST
        
        if 'add_other_official' in request.POST:
        
            #cp = request.POST.copy()
            #cp['other_official-TOTAL_FORMS'] = int(cp['other_official-TOTAL_FORMS']) + 1
            # Get the data from POST
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=request.POST, instance=company)
            prevent_validation_error = True
            
            # <!-- We use the POST data to add anything new -->
            # Saving Added Rows
            for form in new_other_official.forms:
                if form.has_changed():
                    if form.is_valid():
                        #coo_query = CompanyOtherOfficial.objects.filter(company=company, role_name=form.cleaned_data['role_name'], person_name=form.cleaned_data['person_name'])
                        #if not coo_query:
                        form.save()
            ### Al usar sólo el request.POST para obtener y recargar los datos
            ### del formulario, los datos no tenían id de la base de datos (pues
            ### nunca eran cargados de ahí), luego al hacer cualquier modificación
            ### sobre éstos, eran considerados nuevos datos y se guardaban en la BD
            ### junto con la versión antigua (duplicación de líneas).
            ### Ahora estamos creando líneas vacías en la BD al hacer el agregar,
            ### para cargar de la base de datos. Toda línea que quede vacía después de
            ### llenar los datos debería eliminarse al hacer el guardado del formulario
            ### completo.
            
            # Create new empty line in DB
            coo_new = CompanyOtherOfficial(company=company, role_name='', person_name='')
            coo_new.save()
            
            # Reload data from DB
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official',  instance=company)
            
        elif 'delete_other_official' in request.POST:
            prevent_validation_error = True
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=request.POST, instance=company)
            
            # Saving Changed Rows
            for form in new_other_official.forms:
                if form.is_valid():
                    if form.has_changed():
                        form.save()
                            
            # Then we delete the appropiate rows
            for form in new_other_official.deleted_forms:
                if form.is_valid():
                    coo_del = form.cleaned_data['id']
                    coo_del.delete()
                    
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', instance=company)
        
        
            ## Delete from DB
            #new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=request.POST, instance=company)
            #for form in new_other_official.deleted_forms:
            #    if form.is_valid():
            #        coo_query = CompanyOtherOfficial.objects.filter(company=company, role_name=form.cleaned_data['role_name'], person_name=form.cleaned_data['person_name'])
            #        if coo_query:
            #            coo_query[0].delete()
            # Check and delete null data
            #query = CompanyOtherOfficial.objects.all()
            #for q in query:
            #    if q.role_name == None and q.person_name == None:
            #        q.delete()
            ## Regenerate formset without deleted rows
            #new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', instance=company)
        
        else:
            # A form bound to the POST data
            form = CompanyPortadaForm(request.POST, instance=company)
            # If the form is correctly validated
            new_other_official = AddOtherRoleCompanyFormSet(prefix='other_official', data=request.POST, instance=company)
            if new_other_official.is_valid() and form.is_valid():    
                for fm in new_other_official.forms:
                    if fm.has_changed():
                        if fm.is_valid():
                            #coo_query = CompanyOtherOfficial.objects.filter(company=company, role_name=fm.cleaned_data['role_name'], person_name=fm.cleaned_data['person_name'])
                            #if not coo_query:
                            fm.save()
                form.save()
                 ## Delete empty entries
                query = CompanyOtherOfficial.objects.filter(company=company)
                for q in query:
                    if q.role_name == '' and q.person_name == '':
                        q.delete()
                # Delete null entries
                #query = CompanyOtherOfficial.objects.all()
                #for q in query:
                #    if q.role_name == None and q.person_name == None:
                #        q.delete()
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
        
        # A form bound to the POST data
        form = CompanyPortadaForm(request.POST, instance=company)
        
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
