from django import forms
from .models import *
from django.forms import ModelForm


class BlogForm(ModelForm):
    image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = BlogModel
        fields = '__all__'
        exclude = ['author']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        fields = ['content']
