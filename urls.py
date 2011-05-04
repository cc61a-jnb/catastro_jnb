from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('catastro_jnb.censo.views_company',
    url(r'^company/$', 'display_portada_form', name='company'),
    (r'^company/volunteers$', 'display_volunteers_form'),
    (r'^company/infrastructure$', 'display_infrastructure_form'),
    (r'^company/minor_material$', 'display_minor_material_form'),
)

urlpatterns += patterns('catastro_jnb.censo.views_cuerpo',
    url(r'^cuerpo/$', 'display_portada_form', name='cuerpo'),
    (r'^cuerpo/general$', 'display_general_form'),
    (r'^cuerpo/anb$', 'display_anb_form'),
    (r'^cuerpo/mayormaterial$', 'display_mayor_material_form'),
    (r'^cuerpo/infrastructure$', 'display_infrastructure_form'),
)

urlpatterns += patterns('catastro_jnb.censo.views_regional_operations_manager',
    url(r'^regional_operations_manager/$', 'basic_view', name='regional_operations_manager'),
)

urlpatterns += patterns('catastro_jnb.censo.views',
    (r'^$', 'index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)
