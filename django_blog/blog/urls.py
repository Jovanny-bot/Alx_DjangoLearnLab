# blog/urls.py
from django.urls import path
from .views import register, user_login, user_logout, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]

# blog/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/comments/new/', PostDetailView.as_view(), name='post-detail'),  # View a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('comment/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit a post
    path('comment/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post
]

# blog/urls.py
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    search_posts,
)

urlpatterns = [
    # ...
    path('tags/<str:tag_name>/', PostListView.as_view(), name='tag-posts'),
    path('search/', search_posts, name='search-posts'),
]