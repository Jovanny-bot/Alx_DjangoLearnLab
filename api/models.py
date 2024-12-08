from django.db import models

# Create your models here.
#This is the model or table that contains names of authors
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

"""This model called Book, contains title of the book, its publication year, and a foreign key field
'authors' that shows who wrote a certain book."""
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

