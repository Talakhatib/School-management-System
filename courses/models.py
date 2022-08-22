from django.db import models
from users.models import *
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(blank=True,null=True,max_length=100)
    
    def __str__(self) :
        return self.name
    

class Teaches(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
class Enroll(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
class Result(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    grade = models.FloatField(null=True)
    
    def save(self, *args, **kwargs):
        
        object_teacher=Teaches.objects.get(course=self.course)
        self.teacher=object_teacher.teacher
        object_student=Enroll.objects.get(course=self.course)
        self.student=object_student.student
        super(Result, self).save(*args, **kwargs)
    
    
    
    