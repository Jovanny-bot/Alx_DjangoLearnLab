"""
from django.shortcuts import render
from .models import Book

# Create your views here.

def books(request):
  books = Book.objects.all()
  return render(request, "books", "Book")
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



