from dataclasses import field
from rest_framework import serializers
from users.serializers import *
from .models import *

# for get method
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['id','name','descriptions']
# for post/put method 
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['name']
        
class TeachesSerializer(serializers.ModelSerializer):
    teacher =TeacherSerializer()
    course= CourseSerializer()
    class Meta:
        model = Teaches
        fields=["id","course","teacher"]

 # for post/put method of enroll   
class EnrollSerializer(serializers.Serializer):
    student = serializers.IntegerField()
    course=  serializers.IntegerField()
    
    
# for get method of enroll
class EnrollListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()
    course=  CourseListSerializer()
    class Meta:
        model = Student
        fields=['id','student','course']
       
# for get method 
class ResultListSerializer(serializers.ModelSerializer):
    course= CourseListSerializer()
    teacher = TeacherListSerializer()
    student = StudentListSerializer()
    class Meta:
        model = Result
        fields =['id','course','teacher','student','grade']
# for post/put methods
class ResultSerializer(serializers.Serializer):
    course= CourseSerializer()
    teacher = TeacherSerializer()
    student = StudentSerializer()
    class Meta:
        model = Result
        fields =['id','course','teacher','student','grade']
    
    