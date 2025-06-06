# Generated by Django 4.1.7 on 2023-05-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_details',
            name='job_description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='job_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='job_details',
            name='skills_required',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
