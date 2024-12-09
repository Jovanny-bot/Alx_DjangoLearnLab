from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=50)

  def _str_(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length = 50)
  author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = "books")

  def _str_(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length = 50)
  book = models.ManyToManyField(Book, related_name = 'library')

  def _str_(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length = 50)
  library = models.OneToOneField(Library, on_delete = models.CASCADE)

  def _str_(self):
    return self.name