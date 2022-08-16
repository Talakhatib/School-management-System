from dataclasses import field
from rest_framework import serializers
from users.serializers import *
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['id','name','descriptions']
        
class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['name']
        
class TeachesSerializer(serializers.ModelSerializer):
    teacher =teacherSerializer()
    course= courseSerializer()
    class Meta:
        model = Teaches
        fields=["id","course","teacher"]
        
class EnrollSerializer(serializers.ModelSerializer):
    student = studentSerializer()
    course= courseSerializer()
    class Meta:
        model = Student
        fields=['id','student','course']
        
class ResultSerializer(serializers.ModelSerializer):
    course= courseSerializer()
    teacher = teacherSerializer()
    student = studentSerializer()
    class Meta:
        model = Result
        fields =['id','course','teacher','student','grade']
    
    
    