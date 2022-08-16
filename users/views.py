from django.shortcuts import render
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.

class UserDetailAPI(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser,)

    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer= UserSerializer(user)
        return Response(serializer.data)
    
class RegisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,IsAdminUser,)
    serializer_class = RegisterSerializer
    
class TeacherList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]


    def get(self,request,fomrat=None):
        teacher= Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    
    # @swagger_auto_schema(request_body=SnippetSerializer)
    def post(self,request,fomart=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self,pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404


    def get(self,request,pk,formate=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    # @swagger_auto_schema(request_body=SnippetSerializer)
    def put(self,request,pk,formate=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(APIView):
        
    permission_classes = [permissions.IsAuthenticated]


    def get(self,request,fomrat=None):
        student= Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data) 
    
    # @swagger_auto_schema(request_body=SnippetSerializer)
    def post(self,request,fomart=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
class StudentDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404


    def get(self,request,pk,formate=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # @swagger_auto_schema(request_body=SnippetSerializer)
    def put(self,request,pk,formate=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

