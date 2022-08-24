from dataclasses import field
from importlib.metadata import requires
from pdb import post_mortem
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from users.serializers import *
from .models import *
from django.http import Http404
# for get method
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['id','name','descriptions']
# for post/put method 
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['name','descriptions']
#    get teaches     
class TeachesListSerializer(serializers.ModelSerializer):
    teacher =TeacherListSerializer()
    course= CourseSerializer()
    class Meta:
        model = Teaches
        fields=['course','teacher']
        
# post teaches
class TeachesSerializer(serializers.Serializer):
    teacher_id=serializers.IntegerField(required=True)
    course_id=serializers.IntegerField(required=True)
    
    def create(self,data):
        teacher_id=data['teacher_id']
        try:
           teacher=Teacher.objects.get(pk=teacher_id)
        except:
            return Http404
        course_id=data['course_id']
        try:
            
           course=Course.objects.get(pk=course_id)
        except:
            return Http404
        if teacher is not None:
            if course is not None:
                teaches=Teaches()
                teaches.teacher=teacher
                teaches.course=course
                teaches.save()
                
# put Teaches
class TeachesUpdateSerializer(serializers.ModelSerializer):
      course_id=serializers.IntegerField(required=True)
      class Meta:
          model=Teaches
          fields=['course_id']
       
    
    
# post enroll
class EnrollSerializer(serializers.Serializer):
    
    student_id=serializers.IntegerField(required=True)
    course_id=serializers.IntegerField(required=True)
    
    def create(self,data):
        student_id=data['student_id']
        try:
           student=Student.objects.get(pk=student_id)
        except:
            return Http404
        course_id=data['course_id']
        course=Course.objects.get(pk=course_id)
        if student is not None:
            if course is not None:
                enroll=Enroll()
                enroll.student=student
                enroll.course=course
                enroll.save()
# put enroll         
class EnrollUpdateSerializer(serializers.ModelSerializer):
     
      course_id=serializers.IntegerField(required=True)
      class Meta:
          model=Enroll
          fields=['course_id']
       
    
# for get method of enroll
class EnrollListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()
    course=  CourseListSerializer()
    class Meta:
        model = Enroll
        fields=['id','student','course']
        

# for get method 
class ResultListSerializer(serializers.ModelSerializer):
    course= CourseListSerializer()
    teacher = TeacherListSerializer()
    student = StudentListSerializer()
    class Meta:
        model = Result
        fields =['course','teacher','student','grade']
# for post methods
class ResultSerializer(serializers.Serializer):
    teacher_id = serializers.IntegerField(required=True)
    student_id =serializers.IntegerField(required=True)
    course_id=serializers.IntegerField(required=True)
    grade=serializers.FloatField(required=True)
    
    def create(self,data):
        student_id=data['student_id']
        student=Student.objects.get(pk=student_id)
        course_id=data['course_id']
        course=Course.objects.get(pk=course_id)
        teacher_id=data['teacher_id']
        teacher=Teacher.objects.get(pk=teacher_id)
        if student is not None:
            if course is not None:
                if teacher is not None:
                    result=Result()
                    result.student =student
                    result.course=course
                    result.teacher=teacher
                    result.grade=data['grade']
                    result.save()
                 
# for put 
class ResultUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields=['grade']
    
    