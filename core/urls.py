from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('export/employees/', views.export_employees_csv, name='export_employees_csv'),
    path('export/departments/', views.export_departments_csv, name='export_departments_csv'),
]
