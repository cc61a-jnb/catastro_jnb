from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Static media files handling #
###############################

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)

# Generic url's #
#################

urlpatterns += patterns('catastro_jnb.censo.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)

# Company url's #
#################

urlpatterns += patterns('catastro_jnb.censo.views_company',
    url(r'^company/$', 'display_portada_form', name='company'),
    url(r'^company/volunteers$', 'display_volunteers_form', name='company_volunteers'),
    url(r'^company/infrastructure$', 'display_infrastructure_form', name='company_infrastructure'),
    url(r'^company/minor_material$', 'display_minor_material_form', name='company_minor_material'),
)


# Cuerpo url's #
################

urlpatterns += patterns('catastro_jnb.censo.views_cuerpo',
    url(r'^cuerpo/$', 'display_portada_form', name='cuerpo'),
    url(r'^cuerpo/general$', 'display_general_form', name='cuerpo_general'),
    url(r'^cuerpo/anb$', 'display_anb_form', name='cuerpo_anb'),
    url(r'^cuerpo/infrastructure$', 'display_infrastructure_form', name='cuerpo_infrastructure'),
    url(r'^cuerpo/mayor_material$', 'display_mayor_material_form', name='cuerpo_mayor_material'),
    url(r'^cuerpo/alarm_central$', 'display_alarm_central_form', name='cuerpo_alarm_central'),
)

# Reg. Operations Manager url's #
##################################

urlpatterns += patterns('catastro_jnb.censo.views_regional_operations_manager',
    url(r'^regional_operations_manager/$', 'basic_view', name='regional_operations_manager'),
)
