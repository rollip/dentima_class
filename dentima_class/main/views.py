from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import ArchiveAlbumForm
from .mail import *
from .models import Lector, Seminar, ArchiveAlbum, ArchivePhoto
from django.shortcuts import redirect
from .views_helpers import *






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

    if seminar_slug:
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

    else:
        seminars = Seminar.objects.all()
        context = {
            'seminars': seminars,
        }
        return render(request, 'all_seminars_page.html',context)



def archive(request, archive_slug=None):
    if archive_slug:
        # Получение альбома по slug или возврат 404, если не найден
        archive_album = get_object_or_404(ArchiveAlbum, slug=archive_slug)
        # Получение всех фотографий, принадлежащих этому альбому
        archive_photos = ArchivePhoto.objects.filter(album=archive_album)

        # Группировка фотографий на три колонки
        photo_columns = grouped(archive_photos, 3)

        context = {
            'archive_album': archive_album,
            'photo_columns': photo_columns,
        }

        return render(request, 'archive/archive_item.html', context)
    else:
        # Получение всех альбомов
        archives = ArchiveAlbum.objects.all()
        context = {
            'archives': archives,
        }
        return render(request, 'archive.html', context)


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
    else:
        return HttpResponse('404')



def mail(request):
    send_email(request)
    return HttpResponse('200')


def in_dev(request):
    return render(request, 'in_dev.html')


@staff_member_required
def upload_and_display_files(request):
    albums = ArchiveAlbum.objects.all()

    if request.method == 'POST':
        form = ArchiveAlbumForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and get the instance
            album = form.save()
            # Save additional photos if any
            for photo in request.FILES.getlist('photos'):
                ArchivePhoto.objects.create(album=album, photo=photo)
            return redirect('upload_and_display')
    else:
        form = ArchiveAlbumForm()

    return render(request, 'upload.html', {'form': form, 'albums': albums})