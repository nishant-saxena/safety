from django.conf.urls.defaults import patterns,  url

import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='login'),
    # url(r'^safety/', include('safety.foo.urls')),
)
