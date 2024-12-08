from . models import Author, Book
from rest_framework import serializers

#Serializer of book model which will serialize all its three fields
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

"""An author serializer which contains a nested book serializer to return author and all the books 
written by him. """
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']
