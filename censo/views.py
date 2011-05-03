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

# Login form
def login(request): 
    error = None
    notice = None
    # If form has been submitted
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # Check if user correct
        if user is not None:
            role = user.get_profile().latest_role()
            # Check if user doesn't have roles
            if not role:
                error = 'Usted no tiene roles asociados'
            # Else check which role it has
            # If user's role can access /cuerpos/, redirect
            elif role.old_id in [1, 2]:
                django_login(request, user)
                url = '/cuerpo/'
                return HttpResponseRedirect(url)
            # If user's role can access /company/, redirect
            elif role.old_id in [4]:
                django_login(request, user)
                url = '/company/'
                return HttpResponseRedirect(url)
            # Is regional operations manager
            elif role.is_regional_operations_manager():
                django_login(request, user)
                url = '/regional_operations_manager/'
                return HttpResponseRedirect(url)
            # If user's role doesn't grant access, error
            else:
                error = 'Usted no tiene permisos para acceder al sistema'
        #If user is incorrect, error
        else:
            error = 'Nombre de usuario o contraseña incorrectos'
    # If it hasn't been submitted, display any pending notices
    else:   
        form = LoginForm()
        if 'notice' in request.flash:
            notice = request.flash['notice']
    # If user couldn't access anywhere for any reason, return to login form
    return render_to_response('censo/login.html', {
                'form': form,
                'error': error,
                'notice': notice,
            }, context_instance=RequestContext(request))

# Logout form            
@login_required
def logout(request):
    # Simply log user out
    auth.logout(request)
    return HttpResponseRedirect('/login/')

# Main page    
def index(request):
    # If user isn't authenticated, redirect to login form
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    role = request.user.get_profile().latest_role()
    # If user doesn't have roles, notify and redirect to login
    if not role:
        request.flash['notice'] = 'Usted no tiene roles asociados'
        return HttpResponseRedirect('/login')
    # If user's role can access /cuerpos/, redirect
    elif role.old_id in [1, 2]:
        return HttpResponseRedirect('/cuerpo/')
    # If user's role can access /company/, redirect
    elif role.old_id in [4]:
        return HttpResponseRedirect('/company')
    # If user's role doesn't have access, notify and redirect to login
    else:
        request.flash['notice'] = 'Usted no tiene los permisos para acceder al sistema'
        return HttpResponseRedirect('/login')
