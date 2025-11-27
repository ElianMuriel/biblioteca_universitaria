from rest_framework import serializers
from catalog.models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = [
            'id',
            'isbn',
            'titulo',
            'autor',
            'editorial',
            'anio_publicacion',
            'categoria',
            'num_paginas',
            'ubicacion',
            'estado',
            'copias_disponibles',
        ]
