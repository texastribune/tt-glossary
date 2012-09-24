from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import TemplateView

from tx_schools.urls.slug import urlpatterns as schools_urlpatterns

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='tx_schools/landing.html'),
        name='schools_landing'),
)
urlpatterns += schools_urlpatterns
urlpatterns += staticfiles_urlpatterns()
