from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Companie(models.Model):
    company=models.CharField(max_length=20)
    address1=models.CharField(max_length=20)
    address2=models.CharField(max_length=20)
    address3=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    website=models.CharField(max_length=30)
    logo=models.ImageField(upload_to='upload_photos',blank=True,null=True)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.company

class State(models.Model):
    Statename=models.CharField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Statename
    
class District(models.Model):
    Statename=models.ForeignKey(State,on_delete=models.CASCADE)
    District=models.CharField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.District

class Branche(models.Model):
    Branch=models.CharField(max_length=25)
    Branch_code=models.CharField(max_length=25)
    adress=models.CharField(max_length=25)
    Street=models.CharField(max_length=25)
    Statename=models.ForeignKey(State,on_delete=models.CASCADE)
    District=ChainedForeignKey(District,
        chained_field="Statename",
        chained_model_field="Statename",
        show_all=False,
        auto_choose=True,
        sort=True)
    
    Pincode=models.CharField(max_length=25)
    Mobile=models.CharField(max_length=25)
    Email=models.EmailField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Branch
class Enquiry_source(models.Model):
    Enquirysourcename=models.CharField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Enquirysourcename

class Follow_up_statuse(models.Model):
    
    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    Followupstatusname = models.CharField(max_length=250)
    Followupstatus = models.CharField(
        max_length=3,
        choices=YES_NO_CHOICES,
        default='No'
    )
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Followupstatusname
class Qualification(models.Model):
    Qualificationame=models.CharField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Qualificationame

class Syllabus(models.Model):
    Syllabus=models.CharField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Syllabus

class Course(models.Model):
    Course=models.CharField(max_length=25)
    Coursecode=models.CharField(max_length=25)
    Trainers=models.ManyToManyField(User,related_name='UserTrainers',blank=True,limit_choices_to={'is_active':True,'groups__name':'trainerr'},)
    
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Course

class Master_Data(models.Model):
    Name=models.CharField(max_length=25)
    Value=models.CharField(max_length=25)
    Type=models.CharField(max_length=25)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Name