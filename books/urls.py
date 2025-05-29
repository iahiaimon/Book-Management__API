from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AutherViewSet, BookViewSet


router = DefaultRouter()
router.register("authors", AutherViewSet, basename="authors")
router.register("books", BookViewSet, basename="books")


urlpatterns = [
    path("api/", include(router.urls)),
]
