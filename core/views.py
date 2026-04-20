import csv
from django.http import HttpResponse
from django.db.models import Q
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

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        dept = self.request.GET.get('dept')
        status = self.request.GET.get('status')
        
        if q:
            queryset = queryset.filter(
                Q(full_name__icontains=q) | 
                Q(email__icontains=q) |
                Q(phone__icontains=q)
            )
        
        if dept:
            queryset = queryset.filter(department_id=dept)
        
        if status:
            queryset = queryset.filter(status=status)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

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

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | 
                Q(description__icontains=q)
            )
        return queryset

@login_required
def export_employees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Full Name', 'Email', 'Phone', 'Department', 'Date Joined', 'Status'])
    
    employees = Employee.objects.all()
    
    # Apply current filters if any
    q = request.GET.get('q')
    dept = request.GET.get('dept')
    status = request.GET.get('status')
    
    if q:
        employees = employees.filter(Q(full_name__icontains=q) | Q(email__icontains=q))
    if dept:
        employees = employees.filter(department_id=dept)
    if status:
        employees = employees.filter(status=status)

    for emp in employees:
        writer.writerow([
            emp.full_name, 
            emp.email, 
            emp.phone, 
            emp.department.name if emp.department else 'Unassigned', 
            emp.date_joined, 
            emp.status
        ])
    
    return response

@login_required
def export_departments_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="departments.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Name', 'Description'])
    
    departments = Department.objects.all()
    q = request.GET.get('q')
    if q:
        departments = departments.filter(Q(name__icontains=q) | Q(description__icontains=q))
        
    for dept in departments:
        writer.writerow([dept.name, dept.description])
        
    return response
