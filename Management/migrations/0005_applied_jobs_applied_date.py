# Generated by Django 4.1.7 on 2023-05-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0004_rename_student_email_show_jobs_company_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applied_jobs',
            name='applied_date',
            field=models.DateField(null=True),
        ),
    ]
