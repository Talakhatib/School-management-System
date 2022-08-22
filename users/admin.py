from django.contrib import admin
from .models import Student,Teacher,User
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','user','language')
    list_filter = ('language',)
    search_fields = ['user__username']

admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','user','salary')
    search_fields = ['user__username']

admin.site.register(Teacher,TeacherAdmin)

class UserAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
      
    )
admin.site.register(User, UserAdmin)
