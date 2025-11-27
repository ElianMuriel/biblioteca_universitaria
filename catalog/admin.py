from django.contrib import admin
from catalog.models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'isbn', 'autor', 'categoria', 'estado', 'copias_disponibles')
    search_fields = ('titulo', 'isbn', 'autor', 'categoria')
