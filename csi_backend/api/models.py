from django.db import models

# Create your models here.
TYPE = (
        ('prime-core','prime-core'),
        ('core','core'),
        ('sub-heads','sub-heads'),
        ('faculty-cordinator','faculty-cordinator')
    )

DEPT = ( 
        ('President','President'),
        ('Secretary','Secretary'),
        ('Joint Secretary','Joint Secretary'),
        ('Technical','Technical'),
        ('Documentation','Documentation'),
        ('Social','Social'),
        ('Promotion','Promotion'),
        ('Flutter','Flutter'),
        ('Outreach','Outreach'),
        ('Python','Python'),
        ('Java','Java'),
        ('Web','Web'),
        ('C++ & DS','C++ & DS'), 
    )

TYPE_HEAD = (
    ('Head','Head'),
    ('Sub-Head','Sub-Head')
)

class Team(models.Model):
    
    type_member     = models.CharField(choices = TYPE,max_length= 20,null = False)
    display_img     = models.ImageField(upload_to='Member_images',default=None)
    name            = models.CharField(max_length=50,null=False)
    linkdin         = models.CharField(max_length=50) #hyper link
    About           = models.TextField(null=False)
    Post            = models.CharField(choices = DEPT,max_length= 20,default=None,null = False)
    
    def __str__(self):
        return f'{self.name}-{self.Post} {self.type_member}'


class Sig(models.Model):
    name            = models.CharField(max_length=50, primary_key=True, unique=True,null=False)
    Description     = models.TextField(null=False)
    Syllabus        = models.CharField(max_length=50) #hyper link
    Sig_logo        = models.ImageField(default = None,upload_to='Sig_logos')
    Head            = models.CharField(max_length=100,unique=True,null=False)
    subhead         = models.CharField(max_length=100,unique=True,null=True)
    
    def __str__(self):
        return self.name
    

class Event(models.Model):
    name        = models.CharField(max_length=50,default = None,unique=True,null=False)
    Date        = models.DateField(auto_now=False, auto_now_add=False)
    venue       = models.CharField(max_length=50) 
    Description = models.TextField(null=False)
    reg_link    = models.CharField(max_length=50)  #hyper link
    Poster_link = models.CharField(max_length=50) #hyper link
    contact_no  = models.CharField(max_length=15) 
    
    def __str__(self):
        return self.name