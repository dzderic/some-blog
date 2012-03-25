from django.conf.urls.defaults import *

from . import views, forms

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url('^$', views.home, name='home'),
    url('^(?P<page>\d+)/$', views.home, name='post_archive'),
    url('^p/new/$', views.new_post, name='new_post'),
    url('^p/md/$', views.render_markdown, name='render_markdown'),
    url('^p/(?P<slug>[^/]+)/$', views.view_post, name='view_post'),
    url('^p/(?P<slug>[^/]+)/edit/$', views.edit_post, name='edit_post'),
    url('^p/(?P<slug>[^/]+)/delete/$', views.delete_post, name='delete_post'),

    url('^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html',
     'authentication_form': forms.BootstrapAuthenticationForm}, name="login"),
    url('^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
)
