from rest_framework import serializers

from biblioteca_universitaria.catalog.models.libros import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ("id","isbn","titulo","autor","editorial","anio_publicacion","categoria","num_paginas","ubicacion","estado","copias_disponibles")
        read_only_fields = ("id","estado","ubicacion")