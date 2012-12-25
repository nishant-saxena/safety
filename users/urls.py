from django.conf.urls.defaults import patterns, url
#change_password
urlpatterns = patterns('',
    url(r'^$', 'users.views.show_profile', name='profile_view'),
    url(r'^change-password/', 'users.views.change_password', name='change_password'),
 )