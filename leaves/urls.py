from django.urls import path
from . import views

app_name = 'leaves'

urlpatterns = [
    path('', views.LeaveListView.as_view(), name='leave_list'),
]
