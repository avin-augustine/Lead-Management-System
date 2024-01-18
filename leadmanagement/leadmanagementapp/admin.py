from django.contrib import admin
from.models import Companie,State,District,Branche,Enquiry_source,Qualification,Follow_up_statuse,Syllabus,Course,Master_Data
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal=('Trainers',)
admin.site.register(Companie)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Branche)
admin.site.register(Enquiry_source)
admin.site.register(Qualification)
admin.site.register(Syllabus)
admin.site.register(Course,CourseAdmin)
admin.site.register(Master_Data)
admin.site.register(Follow_up_statuse)

