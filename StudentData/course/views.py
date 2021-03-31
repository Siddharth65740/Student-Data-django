from django.shortcuts import render
from .models import course_master
from django.views.generic import CreateView,ListView
# Create your views here.

class newcourse(CreateView):
    model=course_master
    fields = '__all__'


class listview(ListView):
    model = course_master
    fields=['name','description','duration','status','user']
    success_url='home'