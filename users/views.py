from django.shortcuts import render
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class UserDetailAPI(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser,)

    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer= UserSerializer(user)
        return Response(serializer.data)

class ChangePasswordView(generics.UpdateAPIView):
    
#     queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
#     serializer_class = ChangePasswordSerializer
    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def put(self,request,fomart=None):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.validate(request.data) and serializer.validate_old_password(request.user,request.data):
            serializer.update(request.user,request.data)
            return Response({"response":"success",},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
        
       
    
class RegisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,IsAdminUser,)
    serializer_class = RegisterSerializer
    
class TeacherList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]


    def get(self,request,fomrat=None):
        teacher= Teacher.objects.all()
        serializer = TeacherListSerializer(teacher,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=TeacherSerializer)
    def post(self,request,fomart=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response({"response":"success","data":serializer.data},status=status.HTTP_201_CREATED)
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
        serializer = TeacherListSerializer(teacher)
        return Response(serializer.data)


    def delete(self,request,pk,format=None):
        teacher = self.get_object(pk)
        try:
           teacher.delete()
        except: 
             return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK)

class StudentList(APIView):
        
    permission_classes = [permissions.IsAuthenticated]


    def get(self,request,fomrat=None):
        student= Student.objects.all()
        serializer = StudentListSerializer(student,many=True)
        return Response(serializer.data) 
    
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self,request,fomart=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response({"response":"success","data":serializer.data},status=status.HTTP_201_CREATED)
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
        serializer = StudentListSerializer(student)
        return Response(serializer.data)
    

    def delete(self,request,pk,format=None):
        student = self.get_object(pk)
        try:
            student.delete()
        except:
            return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK)   

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

