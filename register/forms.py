from django import forms
from django.contrib.auth.models import User
from utility.util import validateEmail
class RegisterForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    username=forms.CharField()
    email = forms.EmailField()
    password=forms.CharField( widget=forms.PasswordInput(render_value=False), label="Password" )
    repeatpassword=forms.CharField( widget=forms.PasswordInput(render_value=False), label="Repeat Password" )
    
    def is_valid(self):
        result = super(RegisterForm, self).is_valid()

        username=str(self.data.get('username',"")).strip()
         
        if " " in username:
            self._errors['username'] = ["Spaces not allowed in user name"]
        elif len(username)<4 or len(username)>25:
            self._errors['username'] = ["User name length must be between 4 to 25 characters"]
        elif not username.isalnum():
            self._errors['username'] = ["User name must contain alphabets or numbers"]
        elif User.objects.filter(username=username):
            self._errors['username'] = ["User already exists , please pick some other name"]

        first_name=str(self.data.get('first_name',"")).strip()
        if " " in first_name:
            self._errors['first_name'] = ["Spaces not allowed in first name"]
        elif len(first_name)<2 or len(first_name)>55:
            self._errors['first_name'] = ["First name length must be between 2 to 55 characters"]
        elif not first_name.isalnum():
            self._errors['first_name'] = ["First name must contain alphabets or numbers"]

        last_name=str(self.data.get('last_name',"")).strip()
        if " " in last_name:
            self._errors['last_name'] = ["Spaces not allowed in last name"]
        elif len(last_name)<2 or len(last_name)>55:
            self._errors['last_name'] = ["Last name length must be between 2 to 55 characters"]
        elif not last_name.isalnum():
            self._errors['last_name'] = ["Last name must contain alphabets or numbers"]

        email=str(self.data.get('email',"")).strip()
        if not validateEmail(email):
            self._errors['email'] = ["Email is not invalid "]
        elif len(email)>100:
            self._errors['email'] = ["Email length can't more than 100 "]
        password=str(self.data.get('password',"")).strip()
        repeatpassword=str(self.data.get('repeatpassword',"")).strip()
        if " " in password:
            self._errors['password'] = ["Spaces not allowed in password"]
        elif len(password)<4 or len(password)>25:
            self._errors['password'] = ["Password must be between 4 to 25 characters"]
        elif password !=repeatpassword:
            self._errors['password'] = ["Password and confirm password does not match"]
        return self._errors

    def save(self):
        errors=self.is_valid()
        if errors:
            return errors
        username=self.data.get('username',"")
        email=self.data.get('email',"")
        password=self.data.get('password',"")
        first_name=self.data.get('first_name',"")
        last_name=self.data.get('last_name',"")
        user=User.objects.create_user(username, email, password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()


"""
post={}
first_name=post.get("first_name","")
last_name=post.get("last_name","")
username=post.get("username","")
email=post.get("email","")
password=post.get("password","")
repeatpassword=post.get("repeatpassword","")
"""