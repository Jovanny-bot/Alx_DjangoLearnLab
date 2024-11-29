from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for managing CRUD operations on Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

