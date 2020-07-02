from rest_framework import serializers, exceptions
from api2.models import *
class UserDeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_api2
        fields=('username','password')
