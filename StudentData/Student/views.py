from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import student
def home(request):
    return render(request,'users/layout1.html')

class createview(CreateView):
    model = student
    fields = '__all__'
   # success_url = "Student/student_list.html"


class studentlist(ListView):
    model = student
    fields='__all__'
    context_object_name = "student_list"

