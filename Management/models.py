from django.db import models

# Create your models here.
class job_details(models.Model):
    job_ID=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=200)
    company_location=models.CharField(max_length=200)
    company_email=models.EmailField(null=True)
    contact_number=models.IntegerField(null=True)
    job_name=models.CharField(max_length=200,null=True) 
    job_description=models.CharField(max_length=400,null=True)     
    skills_required=models.CharField(max_length=300,null=True)  
    salary=models.IntegerField(null=True)  
    def __str__(self):
        return str(self.company_name)+" "+str(self.job_name)

class applied_jobs(models.Model):
    applied_jobs_ID=models.AutoField(primary_key=True)
    job_ID=models.IntegerField(null=True)
    company_name=models.CharField(max_length=200)
    job_name=models.CharField(max_length=200) 
    student_ID=models.IntegerField(null=True)
    student_name=models.CharField(max_length=200)
    student_phone=models.IntegerField(null=True)
    student_email=models.EmailField(null=True)
    area_of_interest=models.CharField(max_length=200)
    skills_required=models.CharField(max_length=300)
    salary=models.IntegerField(null=True)  
    applied_date=models.DateField(null=True)
    def __str__(self):
        return str(self.student_name)+"    "+str(self.company_name)+"    "+str(self.job_name)


class show_jobs(models.Model):
    showjobs_ID=models.AutoField(primary_key=True)
    student_ID=models.IntegerField(null=True)
    
    job_ID=models.IntegerField(null=True)
    company_name=models.CharField(max_length=200)
    company_location=models.CharField(max_length=200)
    company_email=models.EmailField(null=True)
    contact_number=models.IntegerField(null=True)
    job_name=models.CharField(max_length=200,null=True) 
    job_description=models.CharField(max_length=400,null=True)     
    skills_required=models.CharField(max_length=300,null=True)  
    salary=models.IntegerField(null=True)  
    def __str__(self):
        return str(self.company_name)+" "+str(self.job_name) 
    
class selected_students(models.Model):
    sel_ID=models.AutoField(primary_key=True)
    applied_jobs_ID=models.IntegerField(null=True)
    student_ID=models.IntegerField(null=True)
    job_ID=models.IntegerField(null=True)
    student_name=models.CharField(max_length=200)
    student_phone=models.IntegerField(null=True)
    student_email=models.EmailField(null=True)    
    company_name=models.CharField(max_length=200)
    job_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.company_name)+" "+str(self.job_name)+ " "+str(self.student_name) 
    
