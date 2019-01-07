from django.shortcuts import render, redirect
from .models import Category
from .forms import ProductForm


# Create your views here.
def list_product(request):
    products = Category.objects.all()
    return render(request, 'categories.html', locals())


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_product')

    return render(request, 'products-form.html', {'form': form})


def update_product(request, id):
    product = Category.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list_product')
    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Category.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_product')
    return render(request, 'prod-delete-confim.html', {'product': product})
