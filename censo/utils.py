# coding: utf-8

from django.template import Context, loader

# Check if user can access
def authorize(f):
    def wrap(request, *args, **kwargs):
        # If user isn't authenticated
        if not request.user.is_authenticated():
            request.flash['notice'] = 'Por favor inicie sesión primero'
            return HttpResponseRedirect('/login')
        
        # Get user role
        profile = request.user.get_profile()
        role = profile.latest_role()
        # If user doesn't have roles, error
        if not role:
            request.flash['error'] = 'Usted no tiene roles asociados'
        # If user's role has access to /cuerpo/, redirect
        elif role.old_id in [1, 2]:
            return HttpResponseRedirect('/cuerpo/')
        # If user's role has access to /company/, validate and grant access
        elif role.old_id in [4]:
            return HttpResponseRedirect('/company/')
        # If user's role has access to /regional_operations_manager/, validate and grant access
        elif role.is_regional_operations_manager():
            return f(request, *args, **kwargs)
        # If user's role doesn't have access, error
        else:
            request.flash['error'] = 'Usted no tiene permisos para acceder al sistema'
    
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
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

