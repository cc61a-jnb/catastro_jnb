from censo.forms import CompanyPortadaForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from censo.models import Company

def display_portada_form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SpikeForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            return render_to_response('censo/censo-new.html', {
                'form': form,
                }, context_instance=RequestContext(request),
                )
    company = Company.objects.all()[11]
    initial_data = {
        'address': company.address,
        'phone': company.phone,
        'foundation_date': company.foundation_date,
    }
    
    form = CompanyPortadaForm(initial=initial_data) # si no lo pasamos como intitial, se activa la validacion

    return render_to_response('censo/censo-new.html', {
        'form': form,
        'company': company,
        }, context_instance=RequestContext(request),
        )
