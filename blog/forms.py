from django import forms
from django.db.models import fields
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content']
    