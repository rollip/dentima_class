from django.contrib import admin
from .models import Lector, Seminar, SeminarArchive, Block,Tag

# Inline classes for Block and Tag

class BlockInline(admin.StackedInline):
    model = Block
    extra = 1



class TagInline(admin.StackedInline):
    model = Tag
    extra = 1



# Register Lector
@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register Seminar
@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BlockInline, TagInline]

    def delete_queryset(self, request, queryset):
        for seminar in queryset:
            seminar.delete()


# Register SeminarArchive
@admin.register(SeminarArchive)
class SeminarArchiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    inlines = [BlockInline, TagInline]

    @admin.action(description="Восстановить семинар")
    def restore(self, request, queryset):
        for seminar in queryset:
            seminar.restore()

    actions = [restore]
