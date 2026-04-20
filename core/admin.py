from django.contrib import admin
from .models import Department, Employee, LeaveRequest

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'department', 'status', 'date_joined']
    list_filter = ['department', 'status', 'date_joined']
    search_fields = ['full_name', 'email']

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['employee', 'start_date', 'end_date', 'status', 'approved_by']
    list_filter = ['status', 'start_date', 'end_date']
    search_fields = ['employee__full_name']

