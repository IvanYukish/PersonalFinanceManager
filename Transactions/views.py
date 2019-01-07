from django.shortcuts import render, redirect
from .models import Transactions
from .forms import TransactionsForm


def home_page(request):
    return redirect('login')

def list_transaction(request):
    products = Transactions.objects.all()
    return render(request, 'Transactions.html', locals())


def create_transaction(request):
    form = TransactionsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_transaction')

    return render(request, 'transaction-form.html', {'form': form})


def update_transaction(request, id):
    product = Transactions.objects.get(id=id)
    form = TransactionsForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_transaction')
    return render(request, 'transaction-form.html', {'form': form, 'product': product})


def delete_transaction(request, id):
    product = Transactions.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_transaction')
    return render(request, 'trans-delete-confim.html', {'product': product})
