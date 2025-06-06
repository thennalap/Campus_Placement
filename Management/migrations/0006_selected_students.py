# Generated by Django 4.1.7 on 2023-05-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_applied_jobs_applied_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='selected_students',
            fields=[
                ('sel_ID', models.AutoField(primary_key=True, serialize=False)),
                ('applied_jobs_ID', models.IntegerField(null=True)),
                ('student_ID', models.IntegerField(null=True)),
                ('job_ID', models.IntegerField(null=True)),
                ('student_name', models.CharField(max_length=200)),
                ('student_phone', models.IntegerField(null=True)),
                ('student_email', models.EmailField(max_length=254, null=True)),
                ('company_name', models.CharField(max_length=200)),
                ('job_name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
