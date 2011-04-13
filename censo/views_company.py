from censo.forms import CompanyPortadaForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def display_portada_form(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SpikeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
        else:
            return render_to_response('censo/censo.html', {
                'form': form,
                }, context_instance=RequestContext(request),
                )
            
    form = CompanyPortadaForm() # An unbound form

    return render_to_response('censo/censo.html', {
        'form': form,
        }, context_instance=RequestContext(request),
        )