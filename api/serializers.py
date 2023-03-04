
from api.models import Student
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class StudentSerializer(ModelSerializer):
    class Meta:
        model= Student
        fields ="__all__"

    # all  validation function are code here 
    def validate(self,data):
        if data['roll']>=200:
            raise serializers.ValidationError({'error':'id is more then 200'})
        return data
