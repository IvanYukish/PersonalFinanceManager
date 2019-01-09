from django import forms
from .models import Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', ]


