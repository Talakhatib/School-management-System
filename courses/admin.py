from django.contrib import admin
from .models import *
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

class DoexamAdmin(admin.ModelAdmin):
    list_display = ('id','student','course','date_created')
    search_fields = ['user__username']

admin.site.register(DoExam,DoexamAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','student','teacher','course','grade','date_created')

admin.site.register(Result,ResultAdmin)