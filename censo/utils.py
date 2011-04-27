# coding: utf-8

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
            no_permission_message = 'Usted no tiene permisos para realizar esta acción'
            
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
                request.flash['error'] = 'Usted no tiene roles asociados'
                return HttpResponseRedirect(reverse('login'))

            # assign current role to human readable format                
            if role.is_regional_operations_manager():
                role_name = 'regional_operations_manager'
            elif role.old_id in [1, 2]:
                role_name = 'cuerpo'
            elif role.old_id in [4]:
                role_name = 'company'
            
            print self.roles
            print role_name
                
            # If user has access, grant
            if role_name in self.roles:
                return f(request, *args, **kwargs)
            # redirect to base view in case the user doesn't have access
            else:
                request.flash['error'] = no_permission_message
                return HttpResponseRedirect(reverse(role_name))
        
        return wrap

def render_fields_as_table(fields, column_labels, row_labels):
    template = loader.get_template('tags/fields_table.html')
    
    for idx, row_fields in enumerate(fields):
        row_fields.insert(0, row_labels[idx])
        
    c = Context({
        'fields': fields,
        'column_labels': column_labels,
    })
    return template.render(c)
    
def render_fields_as_list(fields):
    template = loader.get_template('tags/fields_list.html')
        
    c = Context({
        'fields': fields,
    })
    return template.render(c)
    
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

