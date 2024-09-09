from django.shortcuts import render, redirect
from django.views import View
from .models import Employee
from .forms import AddEmployeeForm

# Create your views here.

class Home(View):
    def get(self, request):
        emp_data = Employee.objects.all()

        return render(request,'emp/home.html', {'emp_data':emp_data})
   
class Add_Employee(View):
    def get(self, request):
        fm = AddEmployeeForm()
        return render(request, 'emp/add-employee.html', {'form':fm})

    def post(self, request):
        fm = AddEmployeeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'emp/add-employee.html', {'form':fm})


class Delete_Employee(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        emp_data = Employee.objects.get(id=id)
        emp_data.delete()
        return redirect('/')

class Update_Employee(View):
    def get(self, request,id):
        emps = Employee.objects.get(id=id)
        fm = AddEmployeeForm(instance=emps)
        return render(request, 'emp/update-employee.html', {'form':fm})

    def post(self, request, id):
        emps = Employee.objects.get(id=id)
        fm = AddEmployeeForm(request.POST, instance=emps)
        if fm.is_valid():
            fm.save()
            return redirect('/')
            
        

