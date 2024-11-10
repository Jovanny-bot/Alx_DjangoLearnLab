author_name = "Muvunyi Chriss"

author = Author.objects.get(name=author_name)

#Query all books by a specific author.
books = Book.objects.filter(author=author)

for book in books:
  print(book.title)

#List all books in a library.
library_name = 'Ibitabo'
books = Library.objects.get(name=library_name)
all_library_books = books.all()

for book in all_library_books:
  print(book.title)

#Retrieve the librarian for a library.
librarian = Librarian.objects.get(library="Ikaze Library")
print(librarian.name)