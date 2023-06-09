from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
