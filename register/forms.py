from django import forms
from django.contrib.auth.models import User
from utility.util import validateEmail
from users.models import SiteUser
from captcha.fields import CaptchaField
#
class RegisterFormNonCaptcha(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField(required=False)
    username=forms.CharField()
    email = forms.EmailField()
    password=forms.CharField(required=False, widget=forms.PasswordInput(render_value=False), label="Password" )
    repeatpassword=forms.CharField(required=False,widget=forms.PasswordInput(render_value=False), label="Repeat Password" )
    currentpassword=forms.CharField(show_hidden_initial=False ,required=False, widget=forms.PasswordInput(render_value=False), label="Current Password" )
 
    def validate_username(self):
        username=str(self.data.get('username',"")).strip()
        if " " in username:
            self._errors['username'] = ["Spaces not allowed in user name"]
        elif len(username)<4 or len(username)>25:
            self._errors['username'] = ["User name length must be between 4 to 25 characters"]
        elif not username.isalnum():
            self._errors['username'] = ["User name must contain alphabets or numbers"]
        elif User.objects.filter(username=username):
            self._errors['username'] = ["User already exists , please pick some other name"]

    def validate_first_name(self): 
        first_name=str(self.data.get('first_name',"")).strip()
        self.first_name=first_name
        if not first_name:
            self._errors['first_name'] = ["First name is required"]
        elif " " in first_name:
            self._errors['first_name'] = ["Spaces not allowed in first name"]
        elif len(first_name)<2 or len(first_name)>55:
            self._errors['first_name'] = ["First name length must be between 2 to 55 characters"]
        elif not first_name.isalnum():
            self._errors['first_name'] = ["First name must contain alphabets or numbers"]

    def validate_last_name(self): 
        last_name=str(self.data.get('last_name',"")).strip()
        if last_name:
            if " " in last_name:
                self._errors['last_name'] = ["Spaces not allowed in last name"]
            elif len(last_name)<2 or len(last_name)>55:
                self._errors['last_name'] = ["Last name length must be between 2 to 55 characters"]
            elif not last_name.isalnum():
                self._errors['last_name'] = ["Last name must contain alphabets or numbers"]
    
    def validate_current_password(self,user):    
            currentpassword=str(self.data.get('currentpassword',""))
            if not user.check_password(currentpassword):
                self._errors['currentpassword'] = ["Current password does not match"]
    def validate_email(self):
        email=str(self.data.get('email',"")).strip()
        if not validateEmail(email):
            self._errors['email'] = ["Email is not invalid "]
        elif len(email)>100:
            self._errors['email'] = ["Email length can't more than 100 "]

    def validate_password(self,password,repeatpassword):
        if " " in password:
            self._errors['password'] = ["Spaces not allowed in password"]
        elif len(password)<4 or len(password)>25:
            self._errors['password'] = ["Password must be between 4 to 25 characters"]
        elif password !=repeatpassword:
            self._errors['password'] = ["Password and confirm password does not match"]    


    def save(self):
        super(RegisterFormNonCaptcha, self).is_valid()
        self.validate_username()
        self.validate_first_name()
        self.validate_last_name()
        self.validate_email()
        password=str(self.data.get('password',"")).strip()
        repeatpassword=str(self.data.get('repeatpassword',"")).strip()
        self.validate_password(password,repeatpassword)

        if self._errors:
            return self._errors
        username=self.data.get('username',"")
        email=self.data.get('email',"")
        password=self.data.get('password',"")
        first_name=self.data.get('first_name',"")
        last_name=self.data.get('last_name',"")
        user=User.objects.create_user(username, email, password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        su = SiteUser(u=user)
        su.save()

    def change_password(self, user , post , from_token=False):
        super(RegisterFormNonCaptcha, self).is_valid()
        #As not complete form expected 
        self._errors.clear()
        if "password" in post:
            password=str(self.data.get('password',""))
            repeatpassword=str(self.data.get('repeatpassword',""))
            if not from_token:
                self.validate_current_password(user)
            self.validate_password(password, repeatpassword)
            if  self._errors:
                return self._errors
            user.set_password(password)
        

    def update(self ,user ,post):
        super(RegisterFormNonCaptcha, self).is_valid()
        self._errors.clear()
        #As not complete form expected 
        save_user=email_change=False
        if "first_name" in post:
            self.validate_first_name()
            user.first_name=self.data.get('first_name',"") 
            save_user=True
        if "last_name" in post:
            self.validate_last_name()
            user.last_name=self.data.get('last_name',"")
            save_user=True
        if "email" in post:
            self.validate_email()
            user.email=self.data.get('email',"")
            save_user=email_change=True

        if self._errors:
            for k in self._errors:
                self._errors[k]=self._errors[k][0]
                
            return self._errors
        
        if save_user:
            user.save()
        if email_change:
            pass #Email change save mail etc
class RegisterForm(RegisterFormNonCaptcha):
    captcha = CaptchaField()
    pass #recaptcha = ReCaptchaField(label="I'm a human")