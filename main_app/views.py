from django.shortcuts import redirect, render

from main_app.apps_form import EmployeeForm
from main_app.models import Employee


def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:  # Handle non-POST requests here
        form = EmployeeForm()
    return render(request, 'employee.html', {"form": form})


def show_data(request):
    employees = Employee.objects.all()
    return render(request, 'show_data.html', {"employees": employees})



def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)
    return render(request, 'employee_details.html', {"employee": employee} )
