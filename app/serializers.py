from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30)

    def create(self , validated_data):
        print("Create Method Colled..")
        return Employee.objects.create(**validated_data)
   

    def update(self, employee, validated_data):
        for attr, value in validated_data.items():
            setattr(employee, attr, value)
        employee.save()
        return employee

    

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    
    
