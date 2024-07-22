from django.http import HttpResponse
from django.shortcuts import render
from .mail import *
from .models import Lector,Seminar

import re

# Create your views here.
#     lectors = Lector.objects.all() 'lectors' : lectors,


def extract_youtube_id(url):
    # Регулярное выражение для извлечения ID видео из URL
    pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')
    match = pattern.search(url)
    return match.group(1) if match else None



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
            lectors = [seminar.lector]
            if seminar.lector_2:
                lectors.append(seminar.lector_2)


        except Seminar.DoesNotExist:
            return HttpResponse('404')

        context = {
                'seminar': seminar,
                'lectors': lectors,

            }

        if seminar.video_url:
            video_id = extract_youtube_id(seminar.video_url)
            context['video_id'] = video_id

        return render(request, 'seminar.html',context)


def archive(request):
    return render(request, 'archive.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def documents(request, document_slug=None):
    if document_slug == 'politika_obrabotki_personalnih_dannih':
        return render(request, 'documents/politika_obrabotki_personalnih_dannih.html')
    elif document_slug == 'dogovor_oferta':
        return render(request, 'documents/dogovor_oferta.html')
    elif document_slug == 'credentials':
        return render(request, 'documents/credentials.html')
    else    :
        return HttpResponse('404')



def mail(request):
    send_email(request)
    return HttpResponse('200')


def in_dev(request):
    return render(request, 'in_dev.html')


