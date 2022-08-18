
from email.policy import default
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class SnippetSerializer(serializers.Serializer):

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','first_name','last_name','email']
        
# for get method of students
class StudentListSerializer(serializers.ModelSerializer):
    # username=serializers.ReadOnlyField(source='user.username')
    first_name= serializers.ReadOnlyField(source='user.first_name')
    last_name= serializers.ReadOnlyField(source='user.last_name')
    # email= serializers.ReadOnlyField(source='user.email')
    # phone= serializers.ReadOnlyField(source='user.phone')
    # birthdate= serializers.ReadOnlyField(source='user.birthdate')
    class Meta:
        model= Student
        fields=['id','first_name','last_name','language']
        
        
#   for post and put methods of students      
class StudentSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=20)
    first_name = serializers.CharField(required=True,max_length=30)
    last_name = serializers.CharField(required=True,max_length=30)     
    email = serializers.EmailField(max_length=250,required=True,)
    password = serializers.CharField(max_length=250,write_only=True,required=True, validators=[validate_password])                                
    phone=serializers.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$')])
    birthdate=serializers.DateField()
    language= serializers.CharField(default='en',max_length=2)
    
    def create(self,data):
        user=User()
        user.username=data['username']
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.email=data['email']
        user.phone=data['phone']
        user.birthdate=data['birthdate']
        user.set_password(data['password'])
        user.save()
        student=Student()
        student.user=user
        student.language=data['language']
        student.save()
        

#  for get method of teachers       
class TeacherListSerializer(serializers.ModelSerializer):
    # username=serializers.ReadOnlyField(source='user.username')
    first_name= serializers.ReadOnlyField(source='user.first_name')
    last_name= serializers.ReadOnlyField(source='user.last_name')
    email= serializers.ReadOnlyField(source='user.email')
    # phone= serializers.ReadOnlyField(source='user.phone')
    # birthdate= serializers.ReadOnlyField(source='user.birthdate')
    class Meta:
        model= Teacher
        fields=['id','first_name','last_name','email','salary']
        
        
# for post and put of teachers
class TeacherSerializer(serializers.Serializer):
   
    username = serializers.CharField(required=True, max_length=20)
    first_name = serializers.CharField(required=True,max_length=30)
    last_name = serializers.CharField(required=True,max_length=30)     
    email = serializers.EmailField(max_length=250,required=True,)
    password = serializers.CharField(max_length=250,write_only=True,required=True, validators=[validate_password])                                
    phone=serializers.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$')])
    birthdate=serializers.DateField()
    salary=serializers.IntegerField(default=0)
    
    def create(self,data):
        user = User()
        user.username=data['username']
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.email=data['email']
        user.phone=data['phone']
        user.birthdate=data['birthdate']
        user.set_password(data['password'])
        user.save()
        teacher=Teacher()
        teacher.user=user
        teacher.salary=data['salary']
        teacher.save()
        # user.set_password(data['password'])
        
        
        
        
   
  
        
class LoginSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        
        token = super(LoginSerializer, cls).get_token(user)
        user.save()
       
        token["username"] = user.username
        
        return token
 
    
        
class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    is_admin=serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','is_admin')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
         user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # is_admin=validated_data['is_admin'],
            # is_superuser=validated_data['is_admin']
         )
         user.is_admin=True
         user.is_superuser=True
         user.set_password(validated_data['password'])
         user.save()
         return user
        
        
