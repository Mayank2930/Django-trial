from django import forms

from .models import article

class Blogform(forms.ModelForm):
    class meta:
        model = article
        fields = [
            'title',
            'description'
        ]