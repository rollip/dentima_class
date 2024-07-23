from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify

class Lector(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True,
                            verbose_name='Часть ссылки (автозаполняется)')
    image = models.ImageField(upload_to='lector/images', default='lector/images/empty_lector.jpg', blank=True,
                              null=True, verbose_name='Фотография', help_text='соотношение сторон - квадрат',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    specialization = models.CharField(max_length=300, default='стоматолог', verbose_name='Специализация')
    content = models.TextField()

    class Meta:
        db_table = 'lector'
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SeminarAbstract(models.Model):

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Дата окончания не может быть раньше даты начала')

    name = models.CharField(max_length=200, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True,
                            verbose_name='Часть ссылки (автозаполняется)')
    image = models.ImageField(upload_to='seminar/image', default='seminar/images/empty_seminar.jpg', blank=True,
                              null=True, verbose_name='Картинка',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    video_url = models.URLField(null=True, blank=True, verbose_name="Ссылка на видео YouTube")
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(verbose_name='Окончание')
    lector = models.ForeignKey(to='Lector', on_delete=models.PROTECT, related_name='%(class)s_lector',
                               verbose_name='Лектор 1')
    lector_2 = models.ForeignKey(to='Lector', on_delete=models.PROTECT, related_name='%(class)s_lector_2', blank=True,
                                 null=True, default=None, verbose_name='Лектор 2')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    short_desc = models.TextField()
    pricing = models.TextField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Seminar(SeminarAbstract):

    def delete(self):
        seminar_archive = SeminarArchive.objects.create(
            name=self.name,
            slug=self.slug,
            image=self.image,
            start_date=self.start_date,
            end_date=self.end_date,
            lector=self.lector,
            lector_2=self.lector_2,
            address=self.address,
            short_desc=self.short_desc,
            pricing=self.pricing,
        )
        for block in self.blocks.all():
            block.pk = None
            block.seminar = None
            block.seminar_archive = seminar_archive
            block.save()
        for tag in self.tags.all():
            tag.pk = None
            tag.seminar = None
            tag.seminar_archive = seminar_archive
            tag.save()
        super().delete()

    class Meta:
        db_table = 'seminar'
        verbose_name = 'Семинар'
        verbose_name_plural = 'Семинары'

class SeminarArchive(SeminarAbstract):

    def delete(self):
        pass

    def restore(self):
        seminar = Seminar.objects.create(
            name=self.name,
            slug=self.slug,
            image=self.image,
            start_date=self.start_date,
            end_date=self.end_date,
            lector=self.lector,
            lector_2=self.lector_2,
            address=self.address,
            short_desc=self.short_desc,
            pricing=self.pricing,
        )
        for block in self.blocks.all():
            block.pk = None
            block.seminar = seminar
            block.seminar_archive = None
            block.save()
        for tag in self.tags.all():
            tag.pk = None
            tag.seminar = seminar
            tag.seminar_archive = None
            tag.save()
        super().delete()

    class Meta:
        db_table = 'seminar_archive'
        verbose_name = 'Семинары архив'
        verbose_name_plural = 'Семинары архив'

class Block(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField()
    seminar = models.ForeignKey(Seminar, related_name='blocks', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Семинар")
    seminar_archive = models.ForeignKey(SeminarArchive, related_name='blocks', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Семинар Архив")


class Tag(models.Model):
    text = models.CharField(max_length=20, verbose_name="Тэг")
    seminar = models.ForeignKey(Seminar, related_name='tags', on_delete=models.CASCADE, null=True, blank=True)
    seminar_archive = models.ForeignKey(SeminarArchive, related_name='tags', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text



class ArchiveAlbum(models.Model):
    title = models.TextField(verbose_name='Название альбома')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArchivePhoto(models.Model):
    album = models.ForeignKey(ArchiveAlbum, related_name='photos', on_delete=models.CASCADE, verbose_name='Альбом')
    photo = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
