from django.shortcuts import render

def home(request):
    return render(request,'users/layout1.html')

def login(request):
    return render(request,"users/sign-in.html")
# Create your views here.
