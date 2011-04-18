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

urlpatterns += patterns('jnb_spike.censo.views_company',
    (r'^company/$', 'display_portada_form'),
)

urlpatterns += patterns('jnb_spike.censo.views',
    (r'^$', 'index'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout'),
)
