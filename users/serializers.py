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
        
class StudentSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='user.username')
    first_name= serializers.ReadOnlyField(source='user.first_name')
    last_name= serializers.ReadOnlyField(source='user.last_name')
    email= serializers.ReadOnlyField(source='user.email')
    phone= serializers.ReadOnlyField(source='user.phone')
    birthdate= serializers.ReadOnlyField(source='user.birthdate')
    class Meta:
        model= Student
        fields=["id",'username','first_name','last_name','email','phone','birthdate','language']
        
class studentSerializer(serializers.ModelSerializer):
    
    first_name= serializers.ReadOnlyField(source='user.first_name')
    last_name= serializers.ReadOnlyField(source='user.last_name')
    class Meta:
        model= Student
        fields=['id','first_name','last_name']
        

        
class TeacherSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='user.username')
    first_name= serializers.ReadOnlyField(source='user.first_name')
    last_name= serializers.ReadOnlyField(source='user.last_name')
    email= serializers.ReadOnlyField(source='user.email')
    phone= serializers.ReadOnlyField(source='user.phone')
    birthdate= serializers.ReadOnlyField(source='user.birthdate')
    class Meta:
        model= Teacher
        fields=['username','first_name','last_name','email','phone','birthdate','salary']

class teacherSerializer(serializers.ModelSerializer):
   
    first_name= serializers.ReadOnlyField(source='user.first_name')
    last_name= serializers.ReadOnlyField(source='user.last_name')
    class Meta:
        model= Teacher
        fields=['first_name','last_name']    
        
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
        
        
