from django.urls import path
from . views import list_books, LibraryDetailView

urlpatterns = [
  path("list-books/", list_books, name="list-books"),
  path("library_detail/", LibraryDetailView.as_view, name="library_detail"),
]