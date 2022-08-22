from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group

# Create your models here.

class UserAccountManager(BaseUserManager):
    use_in_migrations = True
    

    def create_user(self, username,email, password=None):
        if not username:
            raise ValueError("Username invalid")
        if not email:
            raise ValueError("Email invalid")

        user = self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        # logger.info("success: create new user with username=%s " % username) 
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username,
                                email=email,
                                password=password)
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        # logger.info("success: create new super user with username=%s " % username) 

class User(AbstractBaseUser, PermissionsMixin):
    """ BmUser model """

    username = models.CharField(blank=False, null=False,
                                max_length=20,
                                unique=True)
    first_name = models.CharField(blank=True, null=True,max_length=30,unique=False)
    last_name = models.CharField(blank=True, null=True,max_length=30,unique=False)     

    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    date_joined = models.DateTimeField(verbose_name='date joined',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',
                                      auto_now_add=True)
                                      
    phone=models.CharField(null=True,max_length=8, validators=[RegexValidator(r'^\d{8}$')])
    birthdate=models.DateField(null=True,blank=True)
    
    groups= models.ManyToManyField(
        Group,
        related_name="user_groups",
        related_query_name="user_group",
        blank=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_ldap = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']
    
    objects = UserAccountManager()

    def has_access(self,action):
        for group in self.groups.all():
            if(group.permissions.filter(codename=action).exists()):
                return True
        return False

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perms(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        ordering = ['id']

    
class Student(models.Model):
    language_choices=[
        ('en','en'),
        ('fr','fr'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    language=models.CharField(max_length=10,choices=language_choices)
    
    def __str__(self):
        return self.user.first_name 
    
class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    salary=models.IntegerField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    