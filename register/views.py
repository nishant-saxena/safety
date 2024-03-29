# Create your views here.
from django.template.response import TemplateResponse
from django.contrib import messages
from forms import RegisterForm
from django.shortcuts import HttpResponseRedirect
def register(request):
    if request.user.is_authenticated():
        messages.add_message(request, messages.INFO, "You already logged in")
        return HttpResponseRedirect("/profile/")
    if request.method=="POST":
        form=RegisterForm(request.POST)
        del form.fields["currentpassword"]
        errors=form.save()
        if not errors:
            messages.add_message(request, messages.INFO, "User saved succesfully")
            return HttpResponseRedirect("/login/")
#        if errors:
#            for each in errors: 
#                messages.add_message(request, messages.ERROR, "\n".join(errors[each]))
    else:
        form=RegisterForm()
        del form.fields["currentpassword"]
    template="register/register.html"
    
    return TemplateResponse(request,template,{"form":form ,})


