# coding: utf-8

import logging

from censo.forms import LoginForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Main page    
def index(request):
    # If user isn't authenticated, redirect to login form
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('login'))
    else:

        return __switch_authenticated_user_role_view(request, request.user)

# Login form
def login(request): 
    error = None
    notice = None
    # If form has been submitted
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        logging.info('Trying user {0} authentication'.format(username))
        user = authenticate(username=username, password=password)
        # Check if user correct
        if user is not None:
            django_login(request, user)
            logging.info("User {0} logged in".format(user.username))
            return __switch_authenticated_user_role_view(request, user)
        # If user is incorrect, error
        else:
            logging.error("User {0}: bad credentials".format(username))
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

# Refactored user role switch in order to DRY
def __switch_authenticated_user_role_view(request, user):
    role = user.get_profile().latest_role()
    # If user doesn't have roles, notify and redirect to login
    if not role:
        request.flash = 'Usted no tiene roles asociados'
        logging.error("user {0} doesn't have any roles".format(username))
        return HttpResponseRedirect(reverse('login'))
    # Else check which role it has
    # If user's role can access /cuerpos/, redirect
    elif role.old_id in [1, 2]:
        url = 'cuerpo'
        return HttpResponseRedirect(reverse(url))
    # If user's role can access /company/, redirect
    elif role.old_id in [4]:
        url = 'company'
        return HttpResponseRedirect(reverse(url))
    # Is regional operations manager
    elif role.is_regional_operations_manager():
        url = 'regional_operations_manager'
        return HttpResponseRedirect(reverse(url))
    # If user's role doesn't grant access, error
    else:
        request.flash = 'Usted no tiene permisos para acceder al sistema'
        logging.error("user {0} doesn't have a valid role for this system".format(username))
        return HttpResponseRedirect(reverse('login'))

# Logout form            
@login_required
def logout(request):
    # Simply log user out
    logging.info("User {0} logged out".format(request.user.username))
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

