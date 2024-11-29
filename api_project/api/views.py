from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer  # Use the BookSerializer