# coding: utf-8

from censo.forms import LoginForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def login(request): 
    error = None
    notice = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            role = user.get_profile().latest_role()
            if not role:
                error = 'Usted no tiene roles asociados'
            elif role.old_id in [1, 2]:
                django_login(request, user)
                error = 'Encuesta de cuerpos aun no implementada'
            elif role.old_id in [4]:
                django_login(request, user)
                url = '/company/'
                return HttpResponseRedirect(url)
            else:
                error = 'Usted no tiene permisos para acceder al sistema'
        else:
            error = 'Nombre de usuario o contraseña incorrectos'
    else:   
        form = LoginForm()
        if 'notice' in request.flash:
            notice = request.flash['notice']
    return render_to_response('censo/login.html', {
                'form': form,
                'error': error,
                'notice': notice,
            }, context_instance=RequestContext(request))
            
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
    
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    role = request.user.get_profile().latest_role()
    if not role:
        request.flash['notice'] = 'Usted no tiene roles asociados'
        return HttpResponseRedirect('/login')
    elif role.old_id in [1, 2]:
        return HttpResponseRedirect('/cuerpo/')
    elif role.old_id in [4]:
        return HttpResponseRedirect('/company')
    else:
        request.flash['notice'] = 'Usted no tiene los permisos para acceder al sistema'
        return HttpResponseRedirect('/login')
