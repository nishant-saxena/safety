from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'safety.views.home', name='home'),
    # url(r'^safety/', include('safety.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^register/', include('register.urls')),
    (r'^login/', include('login.urls')),
    
    url(r'^$', 'home.views.home', name='home'),
    url(r'^logout/', 'login.views.logout', name='logout'),
    url(r'^profile/', 'users.views.show_profile', name='logout'),
 )
import settings
urlpatterns += patterns("django.views",
        url(r'^media(?P<path>.*)/$',
            "static.serve", {
            "document_root": settings.MEDIA_ROOT,
        })
    )



handler404 = 'util.views.error404'
handler500 = 'util.views.error500'

