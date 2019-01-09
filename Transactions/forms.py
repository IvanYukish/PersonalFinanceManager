from django import forms
from django.forms import DateField
from django.contrib.admin.widgets import AdminDateWidget
from .models import Transactions


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['category', 'typeOper', 'suma', 'description']


class GenereteReport(forms.ModelForm):
    olddate = DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    newdate = DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Transactions
        fields = ['typeOper', 'category']
