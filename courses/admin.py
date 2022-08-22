from django.contrib import admin
from .models import Course,Teaches,Enroll,Result
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name','descriptions')

admin.site.register(Course,CourseAdmin)

class TeachesAdmin(admin.ModelAdmin):
    list_display = ('id','teacher','course')

admin.site.register(Teaches,TeachesAdmin)

class EnrollAdmin(admin.ModelAdmin):
    list_display = ('id','student','course')
    search_fields = ['user__username']

admin.site.register(Enroll,EnrollAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','student','teacher','course')

admin.site.register(Result,ResultAdmin)