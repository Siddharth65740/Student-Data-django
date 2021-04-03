from django.shortcuts import render
from .models import course_master
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# Create your views here.

class newcourse(CreateView):
    model=course_master
    fields = '__all__'


class listview(ListView):
    model = course_master
    fields='__all__'
    context_object_name = "course"


class update_view(UpdateView):
    model = course_master
    fields = '__all__'


class delete_view(DeleteView):
    model = course_master
    success_url = '/course/list'

