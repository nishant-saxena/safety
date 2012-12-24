from django.template.response import TemplateResponse
from login.forms import LoginForm
from register.forms import RegisterForm

def home(request):
    template="home/home.html"
    return TemplateResponse(request,template,
                            {"loginform": LoginForm(),"registerform": RegisterForm()})