from django.http import HttpResponse
from django.shortcuts import render
from .mail import *
from .models import Lector,Seminar

# Create your views here.
#     lectors = Lector.objects.all() 'lectors' : lectors,
def index(request):
    seminars = Seminar.objects.all()
    lectors = Lector.objects.all()
    context = {
        'seminars' : seminars,
        'lectors': lectors,
    }
    return render(request,'index.html', context)

def lector(request, lector_slug):
    try:
        lectors = [Lector.objects.get(slug = lector_slug)]
    except Lector.DoesNotExist:
        return HttpResponse('404')

    context = {
        'lectors' : lectors,
    }

    return render(request, 'lector.html', context)




def seminar(request, seminar_slug=None):

    if seminar_slug is None:
        seminars = Seminar.objects.all()
        context = {
            'seminars': seminars,
        }
        return render(request, 'all_seminars_page.html',context)


    else:
        try:
            seminar = Seminar.objects.get(slug=seminar_slug)
            lectors = (seminar.lector, seminar.lector_2)
        except Seminar.DoesNotExist:
            return HttpResponse('404')

        context = {
                'seminar': seminar,
                'lectors': lectors,
            }
        return render(request, 'seminar.html',context)



def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')



def mail(request):
    send_email(request)
    return HttpResponse('200')


def in_dev(request):
    return render(request, 'in_dev.html')