from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Define the BookViewSet for handling all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer for serialization