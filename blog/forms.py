from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', 'Image', 'Category', 'Summary', 'Content', 'is_draft']