from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def lector(request):
    return render(request, 'lector.html')

def seminar(request):
    return render(request, 'seminar.html')

def mail(request):
    return None
