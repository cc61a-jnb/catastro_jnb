from django.template import Context, loader

def render_fields_as_table(fields, column_labels, row_labels, css_class_name='table_fields'):
    template = loader.get_template('tags/fields_table.html')
    
    single_fields = []
    for row_field in fields:
        single_fields.extend(row_field)
        
    errors = combine_fields_errors(single_fields)
            
    for idx, row_fields in enumerate(fields):
        row_fields.insert(0, row_labels[idx])
        
    c = Context({
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
