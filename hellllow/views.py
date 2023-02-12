from django.shortcuts import render
from rest_framework.views import APIView
from .models import Books
from rest_framework.generics import ListCreateAPIView
from .serializers import BookSerializer


class BookViewer(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
