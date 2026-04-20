from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
]
