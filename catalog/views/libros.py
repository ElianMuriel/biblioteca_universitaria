from rest_framework import viewsets, filters
from catalog.models import Libro
from catalog.serializers import LibroSerializer
from catalog.permissions import IsAdminOrReadOnly

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("titulo","isbn")
    ordering_fields = ("titulo","anio_publicacion")