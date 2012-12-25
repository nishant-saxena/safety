# Create your views here.
from django.template.response import TemplateResponse
from django.contrib import messages
from forms import LoginForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY
from users.models import SiteUser
def log_user_in(request,user):
    if SESSION_KEY in request.session:
        if request.session[SESSION_KEY] != str(user.id):
            request.session.flush()
    else:
        request.session.cycle_key()
    request.session[SESSION_KEY] = str(user.id)
    request.session[BACKEND_SESSION_KEY] = user.backend
    if hasattr(request, 'user'):
        request.user = user  #request.user.siteuser is stored at time of register
def logout(request):
    request.session.flush()
    messages.add_message(request, messages.INFO, "Logged out succesfully")
    return HttpResponseRedirect("/")
#from django.contrib.auth.decorators import login_required
#@login_required
def login(request):
    if request.user.is_authenticated():
        messages.add_message(request, messages.INFO, "You already logged in")
        return HttpResponseRedirect("/profile/")
    if request.method=="POST":
        form=LoginForm(request.POST)
        errors=form.is_valid()
        if not errors:
            user=authenticate(username=request.POST.get("username"),password=request.POST.get("password"))
            if user:
                log_user_in(request,user)
                return HttpResponseRedirect("/profile/")
            else:
                messages.add_message(request, messages.ERROR, "User Password mismatch")

    else:
        form=LoginForm()
    template="login/login.html"
    
    return TemplateResponse(request,template,{"form":form})


