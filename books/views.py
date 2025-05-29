from django.shortcuts import render , redirect

from rest_framework.viewsets import ModelViewSet

from .models import Author , Book
from .serializers import (
    AutherSerializer,
    BookSerializer,
)

# Create your views here.


class AutherViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AutherSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer