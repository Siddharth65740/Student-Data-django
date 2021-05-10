from django.shortcuts import render

# Create your views here.
from .models import inquiry
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class newinquiry(LoginRequiredMixin,CreateView):
    model=inquiry
    fields = '__all__'


class listview(LoginRequiredMixin,ListView):
    model = inquiry
    fields='__all__'
    context_object_name = "inquiry_list"


class update_view(LoginRequiredMixin,UpdateView):
    model = inquiry
    fields = '__all__'

class detail_view(LoginRequiredMixin,DetailView):
    model = inquiry

class delete_inquiry(LoginRequiredMixin,DeleteView):
    model = inquiry
    success_url = '/inquiry/list'