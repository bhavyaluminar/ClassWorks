from django.shortcuts import render



from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from employees.models import Employee
from employees.serializers import EmployeeSerializer

#APIVIEW

@api_view(['GET','POST'])
def employeelist(request):#Nonprimarykey based
    # for reading all employee records from Employee Table
    if(request.method=="GET"):
        e=Employee.objects.all()  #reads all the employee records from employee table
        emp=EmployeeSerializer(e,many=True) #converts each record into json using EmployeeSerializer class
        return Response(emp.data,status=status.HTTP_200_OK) #sends response back to client side
    #for creating a new employee record
    if(request.method=="POST"):
        e=EmployeeSerializer(data=request.data)
        if e.is_valid():
            e.save()
            return Response(e.data,status=status.HTTP_201_CREATED)
#primary key based
#Apiview for reading a specific record
@api_view(['GET','PUT','DELETE'])
def employeedetail(request,pk):
    try:
        e = Employee.objects.get(pk=pk)  # Reads that specific record
    except:
        return Response({"message": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if(request.method=="GET"):

        emp=EmployeeSerializer(e) #converts it into Json using Serializer class
        return Response(emp.data,status=status.HTTP_200_OK) #sends Response back to clientside
    if(request.method=="PUT"):

        emp=EmployeeSerializer(e,data=request.data)
        if emp.is_valid():
            emp.save()
        return Response(emp.data,status=status.HTTP_201_CREATED)
    if(request.method=="DELETE"):
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









