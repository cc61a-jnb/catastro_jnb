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
    (r'^company/$', 'display_portada_form'),
    (r'^company/volunteers$', 'display_volunteers_form'),
    (r'^company/infrastructure$', 'display_infrastructure_form'),
    (r'^company/minor_material$', 'display_minor_material_form'),
)

urlpatterns += patterns('catastro_jnb.censo.views',
    (r'^$', 'index'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout'),
)
