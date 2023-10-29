from rest_framework import serializers
from Student.models import User

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class file_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('cv',)