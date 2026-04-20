from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import LeaveRequest

class LeaveListView(LoginRequiredMixin, ListView):
    model = LeaveRequest
    template_name = 'leaves/leave_list.html'
    context_object_name = 'leaves'
    paginate_by = 10
