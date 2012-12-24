from django.conf.urls.defaults import patterns,  url

import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.login, name='login'),
    
    (r'^logout/$', views.logout),

    # url(r'^safety/', include('safety.foo.urls')),
)
