# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


# blog/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

"""
# blog/forms.py
from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        tags = self.cleaned_data['tags'].split(',')
        for tag in tags:
            tag, created = Tag.objects.get_or_create(name=tag.strip())
            post.tags.add(tag)
        if commit:
            post.save()
        return post
"""

# blog/forms.py
from django import forms
from .models import Post
from taggit.form import TagWidget
from django.forms import widgets

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }
