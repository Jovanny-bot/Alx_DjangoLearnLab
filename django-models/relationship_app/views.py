from django.shortcuts import render
from .models import Book

# Create your views here.

def books(request):
  books = Book.objects.all()
  return render(request, "books", "Book")




