from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Employee, Department, LeaveRequest

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'core/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

@login_required
def dashboard(request):
    context = {
        'total_employees': Employee.objects.count(),
        'total_departments': Department.objects.count(),
        'pending_leaves': LeaveRequest.objects.filter(status='pending').count(),
        'active_employees': Employee.objects.filter(status='active').count(),
    }
    return render(request, 'core/dashboard.html', context)

class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = 'core/department_list.html'
    context_object_name = 'departments'
    paginate_by = 10
