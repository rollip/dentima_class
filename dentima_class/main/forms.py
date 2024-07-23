from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Lector, Seminar, SeminarArchive, Block, Tag, ArchiveAlbum


class LectorAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    class Meta:
        model = Lector
        fields = '__all__'

class SeminarAdminForm(forms.ModelForm):
    short_desc = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    pricing = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = Seminar
        fields = '__all__'

class SeminarArchiveAdminForm(forms.ModelForm):
    short_desc = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    pricing = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = SeminarArchive
        fields = '__all__'

class BlockAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    class Meta:
        model = Block
        fields = '__all__'


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ArchiveAlbumForm(forms.ModelForm):

    photos = MultipleFileField()
    class Meta:
        model = ArchiveAlbum
        fields = '__all__'



