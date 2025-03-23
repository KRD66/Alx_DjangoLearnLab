
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
       
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget
from .models import Post


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
class PostForm(forms.ModelForm):
    tags = TagField(widget=LabelWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'cols': 20, 'placeholder': 'Leave a comment...'}),
        }       
        
