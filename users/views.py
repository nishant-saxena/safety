from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.contrib import messages



@login_required
def show_profile(request):
    template="profile/profile.html"
    return TemplateResponse(request,template,{"form":"form"})
