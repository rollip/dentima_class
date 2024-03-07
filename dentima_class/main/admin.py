from django.contrib import admin
from .models import  Lector, Seminar
# Register your models here.

#admin.site.register(Lector)
#admin.site.register(Seminar)

@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



