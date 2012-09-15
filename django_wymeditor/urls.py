from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.contrib import admin

from example.views import ExampleFormView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ExampleFormView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()