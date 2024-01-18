from django.db import models
from leadmanagementapp.models import *
from django.db import models
from smart_selects.db_fields import ChainedForeignKey





Genderchoices=(("Male","Male"),("Female","Female"),("Others","Others"))
yearchoices=(("2018","2018"),("2019","2019"),("2020","2020"),("2021","2021"),("2022","2022"),("2023","2023"))
qualificationchoices=(("BE","BE"),("B.Tech","B.Tech"))
tostaffchoices=(("Roshan","Roshan"),("Mustafa","Mustafa"))

class Student(models.Model):
    # General fieldset
    ENQUIRY_SOURCE_CHOICES = (
        ('Website', 'Website'),
        ('Advertisement', 'Advertisement'),
        ('Friend', 'Friend'),
        # Add more options as needed
    )
    enquiry_source = models.CharField(max_length=50, choices=ENQUIRY_SOURCE_CHOICES)

    # Phone Verification Fieldset
    phone = models.CharField(max_length=15)
    verify_phone_number = models.BooleanField(default=False)

    # Personal Info Fieldset
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    street = models.CharField(max_length=100)
    Statename = models.ForeignKey(State,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=10, blank=True, null=True)


    Gender=models.CharField(max_length=50,choices=Genderchoices)
    Alternative_email=models.EmailField()
    Alternative_Address=models.CharField(max_length=200)
   
    Mobile=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
   
    District=ChainedForeignKey(District,
        chained_field="Statename",
        chained_model_field="Statename",
        show_all=False,  
        auto_choose=False,
        sort=True,)

    
    Whatsapp=models.CharField(max_length=30)

    # Academic Info Fieldset
    college = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50,choices=qualificationchoices)
    Year_of_pass=models.CharField(max_length=50,choices=yearchoices)
    rollno = models.CharField(max_length=20)
    Registration_No = models.CharField(max_length=50)

    # Course Info Fieldset
    course = models.CharField(max_length=50)

    # Photo Fieldset
    photo = models.ImageField(upload_to='student_photos/')

    # Student Call Set Fieldset
    STUDENT_CALL_STATUS_CHOICES = (
        ('Not Contacted', 'Not Contacted'),
        ('Contacted', 'Contacted'),
        # Add more options as needed
    )
    student_call_status = models.CharField(max_length=20, choices=STUDENT_CALL_STATUS_CHOICES)
    next_follow_up_date = models.DateField()
    To_Staff=models.CharField(max_length=50,choices=tostaffchoices)
    comments = models.TextField()

   
    def __str__(self):
        return f"{self.student_name}"
    
class Register(models.Model):
    LAPTOP_CHOICES = (("YES","YES"),("NO","NO"))

    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    phone = models.CharField(max_length=12,verbose_name='Phone')
    email = models.EmailField(max_length=200,blank=True,verbose_name='Email')
    course = models.ForeignKey(Course,max_length=100,on_delete=models.CASCADE,verbose_name='Course')
    batch = models.CharField(max_length=200,verbose_name='Batch')
    trainer=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Trainer")
    have_laptop = models.CharField(max_length=100,choices=LAPTOP_CHOICES,verbose_name="Do you have laptop")
    isactive = models.BooleanField(default=True, verbose_name="Registered")

    def __str__(self):
        return f"{self.name}"

    
    
    
