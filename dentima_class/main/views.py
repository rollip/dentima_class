from django.http import HttpResponse
from django.shortcuts import render
from .mail import *
from .models import Lector,Seminar

# Create your views here.
#     lectors = Lector.objects.all() 'lectors' : lectors,
def index(request):
    seminars = Seminar.objects.all()
    context = {
        'seminars' : seminars,
    }
    return render(request,'index.html', context)

def lector(request, lector_slug):
    try:
        lector = Lector.objects.get(slug = lector_slug)
    except Lector.DoesNotExist:
        return HttpResponse('404')

    context = {
        'lector' : lector,
    }

    return render(request, 'lector.html', context)




def seminar(request,seminar_slug):

    try:
        seminar = Seminar.objects.get(slug=seminar_slug)
        lector = Lector.objects.get(name=seminar.lector.name)

    except Seminar.DoesNotExist:
        return HttpResponse('404')

    context = {
            'seminar': seminar,
            'lector': lector,
        }
    return render(request, 'seminar.html',context)




def mail(request):
    send_email(request)
    return HttpResponse('200')