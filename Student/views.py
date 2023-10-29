from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import user_serializer,file_serializer
from .models import User
from rest_framework import status
from django.contrib.auth import authenticate,login
import re

# Create your views here.
@api_view(['POST'])
def addstudent(request):
    if request.method=="POST":
        student_name=request.data.get('name')
        student_phone=request.data.get('phone')
        student_email=request.data.get('email')
        student_password=request.data.get('password')
        confirm_password=request.data.get('confirmpassword')

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

         
        if len(str(student_phone))!=10:
            return Response("Phone number should be 10 digits")
        elif student_password!=confirm_password:
            return Response("Password and confirm password should be same")
        elif len(student_password) <=6:
            return Response("Minimum 7 characters required for the password")
        elif not re.fullmatch(pattern,student_email):
            return Response("Invalid email address")
        elif User.objects.filter(phonenumber=student_phone).exists():
            return Response("Phone number already exists.Please user another number to register")
        elif User.objects.filter(email=student_email).exists():
            return Response("Email already exists.Please user another email to register")
                   
        else:     
            details=User.objects.create_user(username=student_name,phonenumber=student_phone,email=student_email,password=student_password)
            Token.objects.create(user=details)       
            return Response(data={'student_name':details.username,'response':"User successfully registered",'token':Token.objects.get(user=details).key})


@api_view(['POST'])
def studentlogin(request):
    if request.method=='POST':
        student_phone=request.data.get('phone')
        password=request.data.get('password')
        user=authenticate(request,phonenumber=student_phone,password=password)
        # print("User izzzzzzzzzzz",user)
        # print(type(student_phone))
        if student_phone==9998887770 and password=='management':
            return Response("Mangement Login")
        elif user:
            login(request,user)
            token=Token.objects.get(user=user)
            return Response({'message':'Logged in succesfully','token':token.key,'id':user.student_ID,'name':user.username,'email':user.email})
        else:
            return Response('Invalid Credentials')

#student profile creation
@api_view(['PUT'])
def studentprofile(request,studentid):
    print(studentid,"22222222222222222222222222222222")
    k=User.objects.filter(student_ID=studentid).values()
    print(k[0])
    department=request.data.get('department')
    cgpa=request.data.get('cgpa')
    plus_two=request.data.get('plustwo')
    tenth=request.data.get('tenth')
    area_of_interest=request.data.get('areaofinterest')
    # cv=request.data.get('cv')
    k.update(department=department,previous_cgpa=cgpa,plus_two=plus_two,tenth=tenth,area_of_interest=area_of_interest)
    return Response("Student Profile created")
    


#cv update
@api_view(['PUT'])
def update_file(request,studentid):
    try:
        instance=User.objects.get(student_ID=studentid)
        print(instance,"6"*10)
    except User.DoesNotExist:
        return Response("User does not exists")
    serializer=file_serializer(instance,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['GET'])
def studentdetails(request,studentid):
    student=User.objects.filter(student_ID=studentid)
    print(student,"2"*20)
    serializer=user_serializer(student,many=True)
    return Response(serializer.data)