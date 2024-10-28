from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request,'profile.html')

def education(request):
    return render(request,'education.html')

def experience(request):
    return render(request,'experience.html')

def social(request):
    return render(request,'social.html')