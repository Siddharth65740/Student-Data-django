from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import payment_info
from django.forms import MultiWidget
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import models
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class create_view(LoginRequiredMixin,CreateView):
    model = payment_info
    fields = '__all__'


class paymentListView(LoginRequiredMixin,ListView):
    model= payment_info
    fields ="__all__"
    context_object_name = "payment_list"

class paymentUpdateView(LoginRequiredMixin,UpdateView):
    model = payment_info
    fields = '__all__'

class detail_payment(LoginRequiredMixin,DetailView):
    model = payment_info


class delete_payment(LoginRequiredMixin,DeleteView):
    model = payment_info
    success_url = '/payment/list'


