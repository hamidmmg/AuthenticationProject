from django.urls import path, include
from .views import BookViewer
urlpatterns = [
    path('books/', BookViewer.as_view()),
]
