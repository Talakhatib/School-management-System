from django.shortcuts import render
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class CourseList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        course = Course.objects.all()
        serializer = CourseListSerializer(course,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
class CourseDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
    def get(self,request,pk,formate=None):
        course = self.get_object(pk)
        serializer = CourseListSerializer(course)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)
    def put(self,request,pk,formate=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TeachesList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        teaches = Teaches.objects.all()
        serializer = TeachesSerializer(teaches,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TeachesSerializer)
    def post(self,request):
        serializer = TeachesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TeachesDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk,formate=None):
        teaches = get_object_or_404(Teaches,pk=pk)
        serializer = TeachesSerializer(teaches)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TeachesSerializer)
    def put(self,request,pk,formate=None):
        teaches = get_object_or_404(Teaches,pk=pk)
        serializer = TeachesSerializer(teaches,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        teaches = get_object_or_404(Teaches,pk=pk)
        teaches.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EnrollList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        enroll = Enroll.objects.all()
        serializer = EnrollListSerializer(enroll,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EnrollSerializer)
    def post(self,request):
        serializer = EnrollSerializer(data=request.data)
        if serializer.is_valid():
                serializer.create(request.data)
                return Response(serializer.data,status=status.HTTP_201_CREATED)     
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EnrollDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
  
    def get(self,request,pk):
        enroll = get_object_or_404(Enroll,pk=pk)
        serializer = EnrollListSerializer(enroll)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EnrollPutSerializer)
    def put(self,request,pk): 
        enroll = get_object_or_404(Enroll,pk=pk)
        serializer = EnrollPutSerializer(enroll,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        enroll = get_object_or_404(Enroll,pk=pk)
        enroll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ResultList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]


    def get(self,request):
        result = Result.objects.all()
        serializer = ResultListSerializer(result,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ResultSerializer)
    def post(self,request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ResultDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self,pk):
        try:
            return Result.objects.get(pk=pk)
        except Result.DoesNotExist:
            raise Http404


    def get(self,request,pk,formate=None):
        result = self.get_object(pk)
        serializer = ResultListSerializer(result)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ResultSerializer)
    def put(self,request,pk,formate=None):
        result = self.get_object(pk)
        serializer = ResultSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        result = self.get_object(pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

