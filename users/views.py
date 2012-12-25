from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib import messages
from register.forms import RegisterForm
from django.shortcuts import HttpResponseRedirect
def get_reg_form(request):
    return RegisterForm({"first_name":request.user.first_name ,
                                   "last_name":request.user.last_name , 
                                   "email":request.user.email})
@login_required
def show_profile(request):
    if request.method=="POST":
        registerform=RegisterForm(request.POST)
        errors=registerform.update(request.user,request.POST)
        if not errors:
            messages.add_message(request, messages.INFO, "User updated succesfully")
    else:
        registerform=get_reg_form(request)
    template="profile/profile.html"
    import pdb;
    pdb.set_trace()
    #print request.user.site_user 
    return TemplateResponse(request,template,{"form":registerform})

def change_password(request):
    registerform=get_reg_form(request)
    errors=registerform.change_password(request.user,request.POST)
    if not errors:
        messages.add_message(request, messages.INFO, "Password changed succesfully")
    else:
        messages.add_message(request, messages.ERROR, str(errors))
    return HttpResponseRedirect("/profile/")