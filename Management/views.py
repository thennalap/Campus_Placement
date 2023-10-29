from django.shortcuts import render
from Management.models import job_details,applied_jobs,show_jobs,selected_students
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import jobdetails_serializer,job_serializer,applied_jobs_serializer
from Student.models import User
from rest_framework import status
import re
from django.db.models import Q
import ast
from datetime import date
from django.core.mail import send_mail

# Create your views here.
@api_view(['POST'])
def job_registration(request):
    if request.method=='POST':
        company_name=request.data.get('companyname')
        location=request.data.get('location')
        email=request.data.get('email')
        contact=request.data.get('contact')
        job_name=request.data.get('jobname')
        job_description=request.data.get('description')
        skills=request.data.get('skills')
        salary=request.data.get('salary')
        # serializer=job_serializer(data=request.data)

        details=job_details.objects.create(company_name=company_name,company_location=location,company_email=email,
                                           contact_number=contact,job_name=job_name,job_description=job_description,
                                           skills_required=skills,salary=salary)
        return Response("Job details entered successfuly")
    
@api_view(['GET'])
def jobdetails(request,jobid):
    job=job_details.objects.filter(job_ID=jobid)
    if job.exists():
        serializer=jobdetails_serializer(job,many=True)
        # print(serializer,"mm"*20)
        return Response(serializer.data)
    else:
        return Response("Job not found")

#update job details
@api_view(['PUT'])
def job_details_update(request,jobid):
    # print(jobid,"22222222222222222222222222222222")
    k=job_details.objects.filter(job_ID=jobid).values()
    print(k[0])
    if k.exists():
        jobname=request.data.get('jobname')
        description=request.data.get('description')
        skills=request.data.get('skills')
        salary=request.data.get('salary')
    
    
        k.update(job_name=jobname,job_description=description,skills_required=skills,salary=salary)
        return Response("Job details updated")
    else:
        return Response("No such job")



@api_view(['GET'])
def show_job(request,studentid):
    user_obj=User.objects.filter(student_ID=studentid) 
   
    for i in user_obj:
        interest=i.area_of_interest
        interest_list=ast.literal_eval(interest)
        print(interest_list)       
              
    
        que=Q()
    
        for interest_item in interest_list:
            # print(interest_item)
            
            que|=Q(skills_required__contains=f"'{interest_item}'")
            
            # print(que)
        job_offers=job_details.objects.filter(que)
        # print(job_offers)
        serializer=job_serializer(job_offers,many=True)
        data=serializer.data
        filtered_data = [
            {

                'job_ID': item['job_ID'], 
                'job_name': item['job_name'],
                'company_name':item['company_name']
            }  # Add other desired fields
       for item in data
         ]
        
        filtered_jobs=[
            {
                'job_ID':item['job_ID'],
                'company_name':item['company_name'],
                'company_location':item['company_location'],
                'company_email':item['company_email'],
                'contact_number':item['contact_number'],
                'job_name':item['job_name'],
                'job_description':item['job_description'],
                'skills_required':item['skills_required'],
                'salary':item['salary']
            }
            for item in data
        ]
        # print(filtered_jobs)

        for count,ele in enumerate(filtered_jobs):
            jobid=ele['job_ID']
            companyname=ele['company_name']
            location=ele['company_location']
            email=ele['company_email']
            contact=ele['contact_number']
            jobname=ele['job_name']
            description=ele['job_description']
            skills=ele['skills_required']
            salary=ele['salary']
            
            print(jobid,companyname,location,email,contact,jobname,description,skills,salary)
            if show_jobs.objects.filter(job_ID=jobid,student_ID=studentid).exists():
                return Response("Already exists")
            else:          
                show_jobs.objects.create(student_ID=studentid,job_ID=jobid,company_name=companyname,company_location=location,
                                          company_email=email,contact_number=contact,job_name=jobname,job_description=description,
                                          skills_required=skills,salary=salary)

        
        return Response(filtered_data)
    
    
@api_view(['POST'])
def appliedjobs(request,studentid,jobid):
    student=User.objects.filter(student_ID=studentid)
    for i in student:
        student_ID=i.student_ID
        student_name=i.username
        student_phone=i.phonenumber
        student_email=i.email
        area_of_interest=i.area_of_interest
    # print(student_ID,student_name,student_phone,student_email,area_of_interest)

    jobs=show_jobs.objects.filter(student_ID=studentid,job_ID=jobid)
    for i in jobs:
       
        job_ID=i.job_ID
        company_name=i.company_name
        job_name=i.job_name        
        skills_required=i.skills_required
        salary=i.salary
    # print(job_ID,company_name,job_name,skills_required,salary)

    
    if applied_jobs.objects.filter(job_ID=job_ID,student_ID=student_ID).exists():
        return Response("Already applied")
    else:
        applied_jobs.objects.create(job_ID=job_ID,company_name=company_name,job_name=job_name,student_ID=student_ID,
                                student_name=student_name,student_phone=student_phone,student_email=student_email,
                                 area_of_interest=area_of_interest,skills_required=skills_required,salary=salary,applied_date=date.today())

    # print(student_ID,student_name,student_phone,student_email,area_of_interest)
    return Response("Application submitted succesfully")


@api_view(['GET'])
def view_applied_jobs(request):
    jobs=applied_jobs.objects.all()
    serializer=applied_jobs_serializer(jobs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def view_applied_jobs_by_company(request):
    if request.method=='POST':
        company=request.data.get('companyname')
        jobs=request.data.get('jobname')
    company_list=applied_jobs.objects.filter(company_name=company,job_name=jobs)
    print(company_list)
    serializer=applied_jobs_serializer(company_list,many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_registered_jobs(request,jobid):
    details=job_details.objects.get(job_ID=jobid)
    details.delete()
    return Response("deleted")

@api_view(['POST'])
def selection(request,appliedjobsid):
    if applied_jobs.objects.filter(applied_jobs_ID=appliedjobsid).exists():
        student=applied_jobs.objects.filter(applied_jobs_ID=appliedjobsid)

        for details in student:
            
            company_name=details.company_name
            student_ID=details.student_ID
            student_name=details.student_name
            student_phone=details.student_phone
            student_email=details.student_email 
            job_ID=details.job_ID   
            job_name=details.job_name
            if selected_students.objects.filter(applied_jobs_ID=appliedjobsid).exists():
                return Response("Already exists")
            else:
                selected_students.objects.create(applied_jobs_ID=appliedjobsid, student_ID=student_ID, job_ID=job_ID,company_name=company_name,
                                            student_name=student_name, student_phone=student_phone, student_email=student_email,
                                            job_name=job_name)
                stud=applied_jobs.objects.filter(applied_jobs_ID=appliedjobsid)
                stud.delete()
                return Response("Selected students entered and removed from applied jobs")
    else:
        return Response("Already deleted")
        
        
        
     
   
    





    



    



