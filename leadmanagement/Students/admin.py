from django.contrib import admin
from.models import Student,Register
from django.utils.html import format_html
from django.urls import NoReverseMatch



class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'email', 'dob', 'Mobile','Gender' ]
    Fieldsets = (
        ('General', {
            'fields': ('enquiry_source',),
        }),
        ('Phone Verification', {
            'fields': ('phone', 'verify_phone_number'),
        }),
        ('Personal Info', {
            'fields': ('student_name', 'email','address', 'dob','street', 'state', 'pincode','Gender','Alternative_email','Alternative_Address','Mobile','City','District','Whatsapp'),
        }),
        ('Academic Info', {
            'fields': ('college', 'qualification', 'rollno','Year_of_pass','Registration_No'),
        }),
        ('Course Info', {
            'fields': ('course',),
        }),
        ('Photo', {
            'fields': ('photo',),
        }),
        ('Student Call Status', {
            'fields': ('student_call_status', 'next_follow_up_date','To_Staff',  'comments'),
        }),
        
    )
    def reg_link(self,obj):
        try:
            url= f"/admin/STUDENT/register/add/?name={obj.id}"
            link = f'<a href="{url}">Register</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    reg_link.short_description='Register'
    reg_link.allow_tags=True




class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'course', 'batch', 'have_laptop', 'isactive']


admin.site.register(Student,StudentAdmin)
admin.site.register(Register,RegisterAdmin)