from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import student

class studentview(CreateView):
    model = student
    fields = '__all__'

class list_view(ListView):
    model = student
    fields = '__all__'
    context_object_name = "student_list"

class update_view(UpdateView):
    model = student
    fields = '__all__'

class detail_student(DetailView):
    model = student

class delete_student(DeleteView):
    model = student
    success_url = '/student/list'