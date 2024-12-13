# accounts/urls.py
from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

# accounts/urls.py
from django.urls import path
from .views import FollowUser View, UnfollowUser_View

urlpatterns = [
    path('follow/<int:user_id>/', FollowUser View.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUser View.as_view(), name='unfollow_user'),
]