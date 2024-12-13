from django.shortcuts import render

# Create your views here.
# accounts/views.py
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = response.data['token']
        user = Token.objects.get(key=token).user
        return Response({'token': token, 'user': UserSerializer(user).data})
    
 # accounts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser 

class FollowUser View(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser , id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."})

class UnfollowUser View(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser , id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."})

class ListUsersView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser .objects.all()  # This line ensures you can list all users
    serializer_class = UserSerializer  # Make sure you have a UserSerializer defined
