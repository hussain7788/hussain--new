from django.shortcuts import render,redirect
from app17.models import Employee
from django.contrib import messages

def showIndex(request):
    return render(request,"index.html")

def add_employee(request):
    return render(request,"add_employee.html")

def save_emp(request):
    id = request.POST.get("t1")
    na = request.POST.get("t2")
    sal = request.POST.get("t3")
    # inserting a record into database
    # 1 object means 1 record(1 row)
    Employee(idno=id,name=na,salary=sal).save()

    messages.success(request,"Registration is Successful")
    return redirect('main')

    #return render(request,"index.html",{"message":"Registration is Successful"})


def view_all(request):
    res = Employee.objects.all()
    return render(request,"allEmployees.html",{"data":res})