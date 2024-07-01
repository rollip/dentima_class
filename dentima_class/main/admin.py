from django.contrib import admin
from .models import  Lector, Seminar, SeminarArchive
# Register your models here.

#admin.site.register(Lector)
#admin.site.register(Seminar)

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    prepopulated_fields = {'slug': ('name',)}
    def delete_queryset(self, request, queryset):
        for seminar in queryset:
            seminar.delete()

@admin.register(SeminarArchive)
class SeminarArchiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    pass

'''


    list_display = ('name', 'start_date', 'end_date', 'lector', 'lector_2')
    search_fields = ('name', 'address', 'description')


'''