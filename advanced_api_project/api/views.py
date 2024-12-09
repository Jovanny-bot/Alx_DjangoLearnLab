from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookListView(generics.ListCreateAPIView):
    """View to list all books and create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer  
    permission_classes = [permissions.AllowAny]  # Allow read access to everyone

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, or delete a book."""
    queryset = Book.objects.all()  
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict access to authenticated users                                      