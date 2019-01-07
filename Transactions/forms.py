from django import forms
from .models import Transactions


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['category', 'typeOper', 'suma', 'description']


class GenereteReport(forms.ModelForm):
    olddate = forms.DateField()
    newdate = forms.DateField()
    class Meta:
        model = Transactions
        fields = ['typeOper', 'category']
