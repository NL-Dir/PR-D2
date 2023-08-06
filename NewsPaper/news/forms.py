from django.forms import ModelForm
from .models import Post
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


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


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get_or_create(name='common')[0]
        basic_group.user_set.add(user)
        return user
