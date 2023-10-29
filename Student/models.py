from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import datetime

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)
        
        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def _create_user_phone(self, phonenumber, password,otp, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not phonenumber:
            raise ValueError('Phone number is mandatory')
        
        user = self.model(phonenumber=phonenumber,password=password,otp=otp, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user_phone(self, phonenumber, password,otp, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user_phone(phonenumber, password,otp,**other_fields)

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)



class User(AbstractUser):
    student_ID=models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    phonenumber=models.IntegerField(unique=True)
    email=models.EmailField(null=True,unique=True)
    password=models.CharField(max_length=200)
    department=models.CharField(max_length=250)
    previous_cgpa=models.FloatField(null=True)
    plus_two=models.FloatField(null=True)
    tenth=models.FloatField(null=True)
    area_of_interest=models.CharField(max_length=500,null='True')
    cv=models.FileField(upload_to='cv/')


    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['username','email']
    objects = UserManager()

    def __str__(self):
        return str(self.username)




