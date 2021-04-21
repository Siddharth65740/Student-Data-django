from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import student
from django.contrib.auth.mixins import LoginRequiredMixin


class studentview(LoginRequiredMixin,CreateView):
    model = student
    fields = '__all__'

class list_view(LoginRequiredMixin,ListView):
    model = student
    fields = '__all__'
    context_object_name = "student_list"

class update_view(LoginRequiredMixin,UpdateView):
    model = student
    fields = '__all__'

class detail_student(LoginRequiredMixin,DetailView):
    model = student

class delete_student(LoginRequiredMixin,DeleteView):
    model = student
    success_url = '/student/list'