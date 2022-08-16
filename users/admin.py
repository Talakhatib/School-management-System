from django.contrib import admin
from .models import Student,Teacher,User
# Register your models here.

admin.site.register([Student,Teacher])


class UserAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
      
    )
admin.site.register(User, UserAdmin)
