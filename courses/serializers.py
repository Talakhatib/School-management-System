from dataclasses import field
from importlib.metadata import requires
from rest_framework import serializers
from users.serializers import *
from .models import *

# for get method
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['name','descriptions']
# for post/put method 
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =['name','descriptions']
        
class TeachesSerializer(serializers.ModelSerializer):
    teacher =TeacherSerializer()
    course= CourseSerializer()
    class Meta:
        model = Teaches
        fields=['course','teacher']
# post enroll
class EnrollSerializer(serializers.Serializer):
    
    student_id=serializers.IntegerField(required=True)
    course_id=serializers.CharField(required=True)
    
    def create(self,data):
        student_id=data['student_id']
        student=Student.objects.get(pk=student_id)
        course_id=data['course_id']
        course=Course.objects.get(pk=course_id)
        if student is not None:
            if course is not None:
                enroll=Enroll()
                enroll.student=student
                enroll.course=course
                enroll.save()
#   put enroll         
class EnrollPutSerializer(serializers.ModelSerializer):
      course_id=serializers.IntegerField(required=True)
      class Meta:
          model=Enroll
          fields=['course_id']
      
          
    
 # for post/put method of enroll   
# class EnrollSerializer(serializers.ModelSerializer):
#     student = EnrollStudentSerializer()
#     course=  CourseSerializer()
#     class Meta:
#         model = Enroll
#         fields=['course','student']
    
    
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
    
    