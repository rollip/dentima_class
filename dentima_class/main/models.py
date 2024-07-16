from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


class Lector(models.Model):
    name = models.CharField(max_length=200,unique=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name=' Часть ссылки (автозаполняется)')
    image = models.ImageField(upload_to='lector/images',default='lector/images/empty_lector.jpg', blank=True,null=True, verbose_name='Фотография', help_text='соотношение сторон - квадрат')
    specialization = models.CharField(max_length=100, default='стоматолог', verbose_name='Специализация')
    short_desc = models.TextField(max_length=1000, verbose_name='Короткое описание', help_text='<1000 символов')
    long_desc = models.TextField(max_length=10000, verbose_name='Полное описание  (заголовок в формате <p class="h2 my-3"> День 1 </p>) ', help_text='<10000 символов')


    class Meta:
        db_table = 'lector'
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'
    def __str__(self):
        return self.name




class SeminarAbstract(models.Model):

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.start_date > self.end_date:
            raise ValidationError('Дата окончания не может быть раньше даты начала')

    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True, verbose_name='Часть ссылки (автозаполняется)')
    image = models.ImageField(upload_to='seminar/image', default='seminar/images/empty_seminar.jpg', blank=True, null=True, verbose_name='Картинка')
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(verbose_name='Окончание')
    lector = models.ForeignKey(to='Lector', on_delete=models.PROTECT, related_name='%(class)s_lector', verbose_name='Лектор 1')
    lector_2 = models.ForeignKey(to='Lector', on_delete=models.PROTECT, related_name='%(class)s_lector_2', blank=True, null=True, default=None, verbose_name='Лектор 2')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    type = models.CharField(max_length=50, default='лекция', verbose_name='лекция/практика')
    food = models.CharField(max_length=50, default='кофе-брейк', verbose_name='обед/кофе-брейк')
    full_desc = models.TextField(max_length=10000, verbose_name='Описание (заголовок в формате <p class="h2 mt-5 mb-2"> День 1 </p>)')
    pricing = models.TextField(max_length=3000, verbose_name='Стоимость')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class Seminar(SeminarAbstract):
    def delete(self):
        SeminarArchive.objects.create(
            name=self.name,
            slug=self.slug,
            image=self.image,
            start_date=self.start_date,
            end_date=self.end_date,
            lector=self.lector,
            lector_2=self.lector_2,
            address=self.address,
            type=self.type,
            food=self.food,
            full_desc=self.full_desc,
            short_desc=self.short_desc,
            pricing=self.pricing,
        )
        super().delete()


    class Meta:
        db_table = 'seminar'
        verbose_name = 'Семинар'
        verbose_name_plural = 'Семинары'

class SeminarArchive(SeminarAbstract):
    def delete(self):
        pass

    def restore(self):
        Seminar.objects.create(
            name=self.name,
            slug=self.slug,
            image=self.image,
            start_date=self.start_date,
            end_date=self.end_date,
            lector=self.lector,
            lector_2=self.lector_2,
            address=self.address,
            type=self.type,
            food=self.food,
            full_desc=self.full_desc,
            short_desc=self.short_desc,
            pricing=self.pricing,
        )
        super().delete()

    class Meta:
        db_table = 'seminar_archive'
        verbose_name = 'Cеминары архив'
        verbose_name_plural = 'Cеминары архив'


class Show(models.Model):
    title = models.CharField(max_length=1024)
    slug = models.SlugField(max_length=1024)


class ShowPhoto(models.Model):
    show = models.ForeignKey(
        Show, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField()