from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("name", "email", "text_comments")


class RegisterForm(UserCreationForm):
    ...
