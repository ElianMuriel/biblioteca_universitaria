from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalog.views import LibroViewSet, prestamos_semana, calcular_multa

router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libro')

urlpatterns = [
    path('', include(router.urls)),
    path('prestamos/semana', prestamos_semana, name='prestamos_semana'),
    path('prestamos/multa', calcular_multa, name='calcular_multa'),
]
