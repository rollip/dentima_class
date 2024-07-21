from django.contrib import admin
from .models import  Lector, Seminar, SeminarArchive
# Register your models here.
from .models import Block, Seminar

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'seminar')
    search_fields = ('title', 'content')

class BlockInline(admin.StackedInline):
    model = Block
    extra = 1

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BlockInline]
    def delete_queryset(self, request, queryset):
        for seminar in queryset:
            seminar.delete()

@admin.register(SeminarArchive)
class SeminarArchiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')

    @admin.action(description="Восстановить семинар")
    def restore(self, request, queryset):
        for seminar in queryset:
            seminar.restore()

    actions = [restore]


