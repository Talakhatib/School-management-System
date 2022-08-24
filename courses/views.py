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
            return Response({"response":"success !","data":serializer.data},status=status.HTTP_201_CREATED)
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
            return Response({"response":"success !","data":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        course = self.get_object(pk)
        try:
           course.delete()
        except:
            return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK) 
       
    
class TeachesList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        teaches = Teaches.objects.all()
        serializer = TeachesListSerializer(teaches,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TeachesSerializer)
    def post(self,request):
        serializer = TeachesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response({"response":"success","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TeachesDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk,formate=None):
        teaches = get_object_or_404(Teaches,pk=pk)
        serializer = TeachesListSerializer(teaches)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TeachesUpdateSerializer)
    def put(self,request,pk,formate=None):
        teaches = get_object_or_404(Teaches,pk=pk)
        serializer = TeachesUpdateSerializer(teaches,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"success","data":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        teaches = get_object_or_404(Teaches,pk=pk)
        try:
           teaches.delete()
        except:
            return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK) 
    
    
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
                return Response({"response":"success","data":serializer.data},status=status.HTTP_201_CREATED)     
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EnrollDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
  
    def get(self,request,pk):
        enroll = get_object_or_404(Enroll,pk=pk)
        serializer = EnrollListSerializer(enroll)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EnrollUpdateSerializer)
    def put(self,request,pk): 
        enroll = get_object_or_404(Enroll,pk=pk)
        serializer = EnrollUpdateSerializer(enroll,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"success","data":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        enroll = get_object_or_404(Enroll,pk=pk)
        try:
           enroll.delete()
        except:
            return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK) 
 
class DoExamList(APIView):
        
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        doexam= DoExam.objects.all()
        serializer = DoexamlistSerializer(doexam,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DoexamSerializer)
    def post(self,request):
        serializer = DoexamSerializer(data=request.data)
        if serializer.is_valid():
                serializer.create(request.data)
                return Response({"response":"success","data":serializer.data},status=status.HTTP_201_CREATED)     
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DoExamDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
  
    def get(self,request,pk):
        doexam = get_object_or_404(DoExam,pk=pk)
        serializer = DoexamlistSerializer(doexam)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DoexamUpdateSerializer)
    def put(self,request,pk): 
        doexam = get_object_or_404(DoExam,pk=pk)
        serializer = DoexamUpdateSerializer(doexam,data=request.data)
        if serializer.is_valid():
            serializer.update(pk,request.data)
            return Response({"response":"success","data":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        doexam = get_object_or_404(DoExam,pk=pk)
        try:
           doexam.delete()
        except:
            return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK)    
    
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
            serializer.create(request.data)
            return Response({"respnose":"success","data":serializer.data},status=status.HTTP_201_CREATED)
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

    @swagger_auto_schema(request_body=ResultUpdateSerializer)
    def put(self,request,pk,formate=None):
        result = self.get_object(pk)
        serializer = ResultUpdateSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"success","data":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        result = self.get_object(pk)
        try:
          result.delete()
        except:
            return Response("Error object can't be deleted ",status=status.HTTP_400_BAD_REQUEST)
        return Response("deleted !",status=status.HTTP_200_OK) 

    

