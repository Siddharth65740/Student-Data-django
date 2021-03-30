from django.shortcuts import render
from .models import course_master
from django.views.generic import CreateView
# Create your views here.

class newcourse(CreateView):
    model=course_master
    fields = '__all__'
