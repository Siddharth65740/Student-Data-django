from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import admission
from django.forms import MultiWidget
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.

class create_view(LoginRequiredMixin,CreateView):
    model =admission
    fields = '__all__'


class admissionListView(LoginRequiredMixin,ListView):
    model=admission
    fields ="__all__"
    context_object_name = "admission_list"

class admissionUpdateView(LoginRequiredMixin,UpdateView):
    model = admission
    fields = '__all__'

class detail_student(LoginRequiredMixin,DetailView):
    model = admission

class delete_student(LoginRequiredMixin,DeleteView):
    model = admission
    success_url = '/admission/list'


