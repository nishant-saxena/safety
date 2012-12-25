### http://django-mongodb.org/tutorial.html
###https://docs.djangoproject.com/en/dev/topics/auth/
from django.db import models
# Create your models here.
from django.contrib.auth.models import User 
from djangotoolbox.fields import ListField ,DictField ,EmbeddedModelField

class SiteUser(models.Model):
    # This field is required.
    
    #User
    u = models.OneToOneField(User) 
    #Mobile1
    m1 = DictField() # {'mobile':'number', "verified":"??"} 10 digit number => 91 understood
    #Mobile2
    m2 = DictField() # {"mobile":"number", "verified":"??"} 10 digit number => 91 understood
    #Mobile3
    m3 = DictField() # {"mobile":"number", "verified":"??"} 10 digit number => 91 understood
    #Phone1
    p1 = DictField() # {"phone":"number","std":"stdcode","verified":"??"} 
    #Phone2
    p2 = DictField() # {"phone":"number","std":"stdcode","verified":"??"} 
    
    # Other fields here
    #Friends
    
    f = ListField()  # Will contains _ids of verified friends (user)
    uvf = ListField()  # Will contains _ids of unverified friends (user)
    af = ListField() # Will contains list of anonymous friends 
    d = ListField()  # Will contains _ids of devices

    fo = ListField()  # Will contains whose friend is the user V.imp

    #Other Information
    o=ListField()   # Other information user wants to add [{"title":"Address" ,"value":"b 3 dd puram"} , .....]
    
    def get_mapping(self):
        return {"User":self.u,"mobile1":self.m1 , "mobile2":self.m2 , "mobile3":self.m3 ,
                    "phone1":self.p1 , "phone2":self.p2 , "friends":self.f , "unverified_friends":self.uvf , 
                    "anonymous_friends":self.af ,
                    "devices":self.d , "other_info":self.o  , "friends_of":self.fo ,
                    "NOTE_FRIENDS":"f uvf af d {'i':id ,'t':title }",
                    "NOTE_PHONE":"m1 m2 m3 {'i':id ,'v':0|1  , n:'m1|m2|m3|p1|p2'}" ,
                    "NOTE_fo":"List of friends of "}

    def __str__(self):
        return str(self.get_mapping())

class AnonymousFriends(models.Model):
    #A Site user can have several devices 
    f = EmbeddedModelField('SiteUser')
    fn = models.CharField( max_length=30)
    ln = models.CharField( max_length=30)
    a = models.CharField( max_length=200)
    m1 = models.CharField( max_length=20)
    m2 = models.CharField( max_length=20)
    p1 = models.CharField( max_length=20)
    p2 = models.CharField( max_length=20)
    e = models.EmailField( max_length=50)
    def get_mapping(self):
        return {"first_name":self.fn,"last_name":self.ln,"address":self.a , "mobile1":self.m1
                , "mobile2":self.m2, "phone2":self.p2, "phone2":self.p2 }

#friends {"fn":FName ,"ln":LName , "m1":Mobile, "m2":Mobile, "p1":Phone , "a":"Address" }
class Devices(models.Model):
    #A Site user can have several devices 
    o = EmbeddedModelField('SiteUser')
    #Device ID
    d = models.CharField( max_length=3000, unique=True)
    #Sim Number
    s = models.CharField( max_length=30, unique=True)
    def get_mapping(self):
        return {"owner":self.o,"device_id":self.d , "sim_number":self.s }
    """ e.g. 
    from djangotoolbox.fields import EmbeddedModelField
    
    class Comment(models.Model):  #==== Devices
        created_on = models.DateTimeField(auto_now_add=True)
        author = EmbeddedModelField('Author')
        text = models.TextField()
    
    class Author(models.Model):  #==== SiteUser
        name = models.CharField()
        email = models.EmailField()
    
        def __unicode__(self):
            return '%s (%s)' % (self.name, self.email)
    Comment(
    ...     author=Author(name='Bob', email='bob@example.org'),
    ...     text='The cake is a lie'
    ... ).save()
    >>> comment = Comment.objects.get()
    >>> comment.author
    <Author: Bob (bob@example.org)>

    """

    