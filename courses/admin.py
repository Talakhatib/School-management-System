from django.contrib import admin
from .models import Course,Teaches,Enroll,Result
# Register your models here.
admin.site.register([Course,Teaches,Enroll,Result])