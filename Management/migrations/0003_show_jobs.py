# Generated by Django 4.1.7 on 2023-05-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_alter_job_details_job_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='show_jobs',
            fields=[
                ('showjobs_ID', models.AutoField(primary_key=True, serialize=False)),
                ('applied_jobs_ID', models.IntegerField(null=True)),
                ('job_ID', models.IntegerField(null=True)),
                ('company_name', models.CharField(max_length=200)),
                ('job_name', models.CharField(max_length=200)),
                ('student_ID', models.IntegerField(null=True)),
                ('student_name', models.CharField(max_length=200)),
                ('student_phone', models.IntegerField(null=True)),
                ('student_email', models.EmailField(max_length=254, null=True)),
                ('area_of_interest', models.CharField(max_length=200)),
                ('skills_required', models.CharField(max_length=300)),
                ('salary', models.IntegerField(null=True)),
            ],
        ),
    ]
