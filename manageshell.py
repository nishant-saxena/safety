#For Any module in shine 

#!/usr/bin/env python
import sys
paths =sys.path
for path in paths :
    #if path.startswith("/usr/local/"):
    if "dist-packages"  in path: 
        pp=path.split("dist-packages")
        DJANGO_ROOT=pp[0]+"dist-packages/django"
        PYTHON_ROOT=pp[0]+"dist-packages"
        break
    if "site-packages"  in path: 
        pp=path.split("site-packages")
        DJANGO_ROOT=pp[0]+"site-packages/django"
        PYTHON_ROOT=pp[0]+"site-packages"
        break

import os
import site
import logging
from datetime import datetime
last_dir= os.path.abspath(".").split("/")[-1]
PROJECT_PATH= os.path.abspath(".").split(last_dir)[0]+last_dir
#DJANGO_ROOT = '/usr/local/lib/python2.7/dist-packages/django'
#PROJECT_PATH='/home/nishant/Desktop/svnshine/ffprojects_sumoplus/trunk/'
#site.addsitedir('/usr/local/lib/python2.7/dist-packages/')
site.addsitedir(PYTHON_ROOT)
sys.path.append(DJANGO_ROOT)
sys.path.append(PROJECT_PATH)
from django.core.management import setup_environ
import settings
setup_environ(settings)
os.chdir(PROJECT_PATH)
if __name__=="__main__":
    if sys.argv[1]=="register":
        """
<QueryDict: {u'username': [u''], u'firstname': [u''], u'lastname': [u''], u'csrfmiddlewaretoken': [u'862543729671aed538359505beb9f350'], u'password': [u''], u'repeatpassword': [u''], u'email': [u'']}>
(Pdb) type(request.POST)
<class 'django.http.QueryDict'>
(Pdb) dir(request)
['COOKIES', 'FILES', 'GET', 'META', 'POST', 'REQUEST', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cookies', '_encoding', '_files', '_get_cookies', '_get_encoding', '_get_files', '_get_get', '_get_post', '_get_raw_post_data', '_get_request', '_get_upload_handlers', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post', '_post_parse_error', '_raw_post_data', '_read_started', '_set_cookies', '_set_encoding', '_set_get', '_set_post', '_set_upload_handlers', '_stream', '_upload_handlers', 'build_absolute_uri', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_host', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'raw_post_data', 'read', 'readline', 'readlines', 'session', 'upload_handlers', 'user', 'xreadlines']
(Pdb) type(request)
<class 'django.core.handlers.wsgi.WSGIRequest'>

        """
        print "Test register flow"
