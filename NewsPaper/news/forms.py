from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'categoryType', 'title', 'text']
        widgets = {
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'postCategory': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
            'categoryType': forms.Select(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            })

        }
