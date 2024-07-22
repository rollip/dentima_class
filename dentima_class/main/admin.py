from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Lector, Seminar, SeminarArchive, Block, Tag

# Define admin form classes with CKEditor5
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

# Inline classes for Block and Tag
class BlockInline(admin.StackedInline):
    model = Block
    form = BlockAdminForm
    extra = 0

class TagInline(admin.StackedInline):
    model = Tag
    extra = 0

# Register Lector with custom form
@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    form = LectorAdminForm
    prepopulated_fields = {'slug': ('name',)}

# Register Seminar with custom form
@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    form = SeminarAdminForm
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BlockInline, TagInline]

    def delete_queryset(self, request, queryset):
        for seminar in queryset:
            seminar.delete()

# Register SeminarArchive with custom form
@admin.register(SeminarArchive)
class SeminarArchiveAdmin(admin.ModelAdmin):
    form = SeminarArchiveAdminForm
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    inlines = [BlockInline, TagInline]

    @admin.action(description="Восстановить семинар")
    def restore(self, request, queryset):
        for seminar in queryset:
            seminar.restore()

    actions = [restore]
