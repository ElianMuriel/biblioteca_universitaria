# catalog/urls.py
from rest_framework.routers import DefaultRouter
from catalog.views.libros import LibroViewSet


router = DefaultRouter()
router.register(r'categories', LibroViewSet, basename='libros')

urlpatterns = router.urls
