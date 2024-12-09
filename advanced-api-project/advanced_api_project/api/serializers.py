from . models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = ['name', 'books']
