from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


class Lector(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='lectors/images',blank=True,null=True)
    specialization = models.CharField(max_length=100, default='стоматолог')
    short_desc = models.TextField(max_length=2000)
    long_desc = models.TextField(max_length=10000)


    class Meta:
        db_table = 'lector'
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'
    def __str__(self):
        return self.name


class Seminar(models.Model):

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.start_date > self.end_date:
            raise ValidationError('Дата окончания не может быть раньше даты начала')

    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    image_1 = models.ImageField(upload_to='seminar/images',blank=True,null=True)
    image_2 = models.ImageField(upload_to='seminar/images',blank=True,null=True)
    background_image = models.ImageField(upload_to='seminar/background',default='seminar/background/background7.jpg',blank=True,null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    lector = models.ForeignKey(to=Lector, on_delete=models.PROTECT, related_name='lector')
    lector_2 = models.ForeignKey(to=Lector, on_delete=models.PROTECT, related_name='lector_2', blank=True, null=True, default=None)
    address = models.CharField(max_length=100, unique=False)
    type = models.CharField(max_length=50, default='лекция')
    food = models.CharField(max_length=50,  default='кофе-брейк')
    description = models.TextField(max_length=10000)
    pricing = models.TextField(max_length=3000)

    class Meta:
        db_table = 'seminar'
        verbose_name = 'Семинар'
        verbose_name_plural = 'Семинары'

    def __str__(self):
        return self.name


