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

# blog/urls.py
from django.urls import path
from .views import PostByTagListView

urlpatterns = [
    # ...
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
    # ...
]

# blog/views.py
from django.views.generic import ListView
from .models import Post
from taggit.models import Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = Tag.objects.get(slug=tag_slug)
        return Post.objects.filter(tags__in=[tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag_slug']
        return context