# coding: utf-8

import logging

from censo.forms import LoginForm
from censo.models import Cuerpo
from censo.models import Region

from djangoflash.decorators import keep_messages

from django.conf import settings
from django.db import connections
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required

# Main page
@keep_messages # needed for not deleting received flash messages and handle them to next view
def index(request):
    # If user isn't authenticated, redirect to login form
    if not request.user.is_authenticated():
        return redirect('login')

    profile = request.user.get_profile()

    if profile.is_administrator():
        return redirect('administrator')

    role = profile.role_id
    
    # If user doesn't have roles, notify and redirect to login
    if not role:
        request.flash['error'] = 'Usted no tiene roles asociados'
        logging.error("user %s doesn't have any roles", request.user.username)
        return redirect('login')

    # check which role it has
    if profile.is_company_manager():
        return redirect('company', company_id=profile.company.old_id)
    elif profile.is_cuerpo_manager():
        return redirect('cuerpo', cuerpo_id=profile.company.cuerpo.old_id)
    elif profile.is_regional_operations_manager():
        region_id = profile.get_region_id()
        return redirect('regional_operations_manager', region_id=region_id)
    # If user's role doesn't grant access, error
    else:
        request.flash['error'] = 'Usted no tiene permisos para acceder al sistema'
        return redirect('login')

# Login form
def login(request):
    error = None
    notice = None
    # If form has been submitted
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        logging.info('Trying user %s authentication', username)
        user = authenticate(username=username, password=password)
        # Check if user correct
        if user is not None:
            django_login(request, user)
            logging.info("User %s logged in", user.username)
            
            if user.get_profile().is_administrator():
                cursor = connections['principal'].cursor()
                Region.fetch_all(cursor)
                cursor.close()
            return index(request)
        # If user is incorrect, error
        else:
            logging.error("User %s: bad credentials", username)
            request.flash['error'] = 'Nombre de usuario o contraseña incorrectos'
    # If it hasn't been submitted, display any pending notices
    else:   
        form = LoginForm()
    # If user couldn't access anywhere for any reason, return to login form
    return render_to_response('login.html', {
                'form': form,
            }, context_instance=RequestContext(request))

# Logout form
@login_required
def logout(request):
    # Simply log user out
    request.flash['notice'] = 'Ha salido exitosamente del sistema'
    logging.info("User %s logged out", request.user.username)
    auth.logout(request)
    return redirect('login')

def server_error(request, template_name='500.html'):
    "Always includes MEDIA_URL"
    from django.http import HttpResponseServerError
    t = loader.get_template(template_name)
    return HttpResponseServerError(t.render(Context({'MEDIA_URL': settings.MEDIA_URL})))