# coding: utf-8

import logging

from functools import wraps
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Check if user has the role required to the decorated view
class authorize(object):
    """
    roles must contain at least one of these: 'regional_operations_manager', 'cuerpo', 'company'
    """
    def __init__(self, roles=()):
        self.roles = roles

    def __call__(self, f):

        @wraps(f)
        def wrap(request, *args, **kwargs):
            # If user isn't authenticated
            if not request.user.is_authenticated():
                request.flash['notice'] = 'Por favor inicie sesión primero'
                return HttpResponseRedirect(reverse('login'))

            # Get user role
            profile = request.user.get_profile()
            role = profile.latest_role()
            role_name = None

            # If user doesn't have roles, error
            if not role:
                logging.error("User {0} doesn't have a role".format(request.user.username))
                request.flash['error'] = 'Usted no tiene roles asociados'
                return HttpResponseRedirect(reverse('login'))

            # assign current role to human readable format
            if role.is_regional_operations_manager():
                role_name = 'regional_operations_manager'
            elif role.old_id in [1, 2]:
                role_name = 'cuerpo'
            elif role.old_id in [4]:
                role_name = 'company'

            # If user has access, grant
            if role_name in self.roles:
                return f(request, *args, **kwargs)
            # redirect to base view in case the user doesn't have access
            else:
                request.flash['error'] = 'Usted no tiene permisos para realizar esta acción'
                logging.info("User {0} doesn't have permission to access {1}".format(request.user.username, request.path))
                return HttpResponseRedirect(reverse(role_name))

        return wrap

def render_fields_as_table(fields, column_labels, row_labels, css_class_name='table_service_acts'):
    template = loader.get_template('tags/fields_table.html')

    #helper text array
    helper_text = []
    single_fields = []
    for row_field in fields:
        single_fields.extend(row_field)

    for index, item in enumerate(fields):
        helper_text.append(item[0].help_text)
        print item[0].help_text
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
