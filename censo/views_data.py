from authentication import authorize
from censo.models import *
from django.db import connections
from django.utils import simplejson
from django.http import HttpResponse


@authorize(roles=('administrator', 'regional_operations_manager', 'cuerpo'))
def get_related(request, class_name, entity_id):
    Class = eval(class_name.capitalize())
    entity = Class.objects.get(old_id=entity_id)
    
    cursor = connections['principal'].cursor()
    children = entity.fetch_all_related(cursor)
    cursor.close()
    return HttpResponse(
        simplejson.dumps(children),
        content_type = 'application/javascript; charset=utf8'
    )
