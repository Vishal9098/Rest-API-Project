from .models import Employee
from django.http import JsonResponse
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User 
from rest_framework .decorators import api_view
from rest_framework import status
from rest_framework .response import Response

@api_view(['GET' , 'POST'])
def employeelist(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['DELETE' , 'GET' , 'PUT'])      
def employeeDetailView(request,pk):
    try:
        employee = Employee.objects.get(pk=pk )
    except Employee.DoesNotExist:
        return Response(status=404)


    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee ,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

 
def userlist(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

def aad(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
