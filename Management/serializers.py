from rest_framework import serializers
from Management.models import job_details,applied_jobs

class jobdetails_serializer(serializers.ModelSerializer):
    class Meta:
        model=job_details
        fields='__all__'

class job_serializer(serializers.ModelSerializer):
    class Meta:
        model=job_details
        fields='__all__'

class applied_jobs_serializer(serializers.ModelSerializer):
    class Meta:
        model=applied_jobs
        fields='__all__'
