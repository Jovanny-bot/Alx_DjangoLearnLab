"""
from django.shortcuts import render
from .models import Book

# Create your views here.

def books(request):
  books = Book.objects.all()
  return render(request, "books", "Book")
"""
"""
from django.shortcuts import render
from .models import Book, Library

def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
"""
# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(View):
    def get(self, request, pk):
        library = get_object_or_404(Library, pk=pk)
        return render(request, 'library_detail.html', {'library': library})

