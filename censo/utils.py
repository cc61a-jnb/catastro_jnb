from django.template import Context, loader

def render_fields_as_table(fields, column_labels, row_labels, css_class_name='table_fields'):
    template = loader.get_template('tags/fields_table.html')
    
    for idx, row_fields in enumerate(fields):
        row_fields.insert(0, row_labels[idx])
        
    c = Context({
        'fields': fields,
        'column_labels': column_labels,
        'css_class_name': css_class_name,
    })
    return template.render(c)
    
def render_fields_as_list(fields, css_class_name='list_fields'):
    template = loader.get_template('tags/fields_list.html')
        
    c = Context({
        'fields': fields,
        'css_class_name': css_class_name,
    })
    return template.render(c)
    
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

