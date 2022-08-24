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
# for get 
class DoexamlistSerializer(serializers.ModelSerializer):
    student=StudentListSerializer()
    course=CourseListSerializer()
    class Meta:
        model=DoExam
        fields=['id','student','course']
# post method
class DoexamSerializer(serializers.Serializer):
    student_id=serializers.IntegerField(required=True)
    course_id=serializers.IntegerField(required=True)
    
    def create(self,data):
        student_id=data['student_id']
        course_id=data['course_id']
        try:
           enroll=Enroll.objects.get(student=student_id,course=course_id)
        except:
            raise Http404
        if enroll:
                student=Student.objects.get(pk=student_id)
                course=Course.objects.get(pk=course_id)
                doexam=DoExam()
                doexam.student=student
                doexam.course=course
                doexam.save()
# put method
class DoexamUpdateSerializer(serializers.ModelSerializer):
      course_id=serializers.IntegerField(required=True)
      
      class Meta:
          model= DoExam
          fields=['course_id']
          
      def update(self,pk ,data):
        course_id=data['course_id']
        try:
          course=Course.objects.get(pk=course_id)
        except:
            raise Http404
        exam=DoExam.objects.get(pk=pk)
        student=exam.student
        try:
           course_check=Enroll.objects.get(student=student,course=course_id)
        except:
            raise Http404
        if course_check :
            doexam=DoExam.objects.get(pk=pk)
            doexam.course=course
            doexam.save()
        
     
      
      
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
            raise Http404
        course_id=data['course_id']
        try:
            course=Course.objects.get(pk=course_id)
        except:
            raise Http404
        if teacher and course:
                teaches=Teaches()
                teaches.teacher=teacher
                teaches.course=course
                teaches.save()
                
# put Teaches
class TeachesUpdateSerializer(serializers.ModelSerializer):
      class Meta:
          model=Teaches
          fields=['course']
       
    
    
# post enroll
class EnrollSerializer(serializers.Serializer):
    
    student_id=serializers.IntegerField(required=True)
    course_id=serializers.IntegerField(required=True)
    
    def create(self,data):
        student_id=data['student_id']

        course_id=data['course_id']
        try:
           student=Student.objects.get(pk=student_id)
        except:
            raise Http404
        try:
          course=Course.objects.get(pk=course_id)
        except:
            raise Http404
        if student and course:
                enroll=Enroll()
                enroll.student=student
                enroll.course=course
                enroll.save()
# put enroll         
class EnrollUpdateSerializer(serializers.ModelSerializer):
      class Meta:
          model=Enroll
          
          fields=['course']
       
    
# for get method of enroll
class EnrollListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer()
    course=  CourseSerializer()
    class Meta:
        model = Enroll
        fields=['id','student','course']
        

# for get method 
class ResultListSerializer(serializers.ModelSerializer):
    course= CourseSerializer()
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
        course_id=data['course_id']
        teacher_id=data['teacher_id']
        try:
          student_check=DoExam.objects.get(course=course_id,student=student_id)
        except:
            raise Http404
        try:
          teacher_check=Teaches.objects.get(course=course_id,teacher=teacher_id)
        except:
            raise Http404
        if student_check and teacher_check:
     
                    course=Course.objects.get(pk=course_id)
                    student=Student.objects.get(pk=student_id)
                    teacher=Teacher.objects.get(pk=teacher_id)

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
    
    