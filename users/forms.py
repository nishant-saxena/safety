from django import forms
from django.contrib.auth.models import User
from utility.util import validateEmail
class ProfileForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField( widget=forms.PasswordInput(render_value=False), label="Password" )
    
    def is_valid(self):
        result = super(ProfileForm, self).is_valid()
        username=str(self.data.get('username',"")).strip()
        if " " in username:
            self._errors['username'] = ["Spaces not allowed in user name"]
        elif len(username)<4 or len(username)>25:
            self._errors['username'] = ["User name length must be between 4 to 25 characters"]
        elif not username.isalnum():
            self._errors['username'] = ["User name must contain alphabets or numbers"]

        
        password=str(self.data.get('password',"")).strip()
        if " " in password:
            self._errors['password'] = ["Spaces not allowed in password"]
        elif len(password)<4 or len(password)>25:
            self._errors['password'] = ["Password must be between 4 to 25 characters"]
        return self._errors


