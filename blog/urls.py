from django.conf.urls.defaults import *

from . import views, forms

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^$', views.home),
    ('^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html',
     'authentication_form': forms.BootstrapAuthenticationForm}),
    ('^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
