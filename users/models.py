### http://django-mongodb.org/tutorial.html
###https://docs.djangoproject.com/en/dev/topics/auth/
from django.db import models
# Create your models here.
from django.contrib.auth.models import User 
from djangotoolbox.fields import ListField ,EmbeddedModelField

class SiteUser(models.Model):
    # This field is required.
    
    #User
    u = models.OneToOneField(User) 
    #Mobile1
    m1 = EmbeddedModelField() # {"mobile":"number", "verified":"??"} 10 digit number => 91 understood
    #Mobile2
    m2 = EmbeddedModelField() # {"mobile":"number", "verified":"??"} 10 digit number => 91 understood
    #Mobile3
    m3 = EmbeddedModelField() # {"mobile":"number", "verified":"??"} 10 digit number => 91 understood
    #Phone1
    p1 = EmbeddedModelField() # {"phone":"number","std":"stdcode","verified":"??"} 
    #Phone2
    p2 = EmbeddedModelField() # {"phone":"number","std":"stdcode","verified":"??"} 
    
    # Other fields here
    #Friends
    f = ListField()  # Will contains _ids of user
    #Anonymous Friends
    af = ListField() # Will contains list of anonymous friends 
            #{"id":"","name":name , "address",address , others : othersinfoupt2000chars}
    #devices
    d = ListField()  # Will contains _ids of devices
    #Other Information
    o=ListField()   # Other information user wants to add [{"title":"Address" ,"value":"b 3 dd puram"} , .....]
    
    def get_mapping(self):
        return {"User":self.u,"mobile1":self.m1 , "mobile2":self.m2 , "mobile3":self.m3 ,
                    "phone1":self.p1 , "phone2":self.p2 , "friends":self.f , "anonymous_friends":self.af ,
                    "devices":self.d , "other_info":self.o  }

        

class Devices(models.Model):
    #Owner
    o = EmbeddedModelField('SiteUser')
    #Device ID
    d = models.CharField( max_length=3000, unique=True)
    #Sim Number
    s = models.CharField( max_length=30, unique=True)
    def get_mapping(self):
        return {"owner":self.o,"device_id":self.d , "sim_number":self.s }

    