from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def products(request):
    title = 'продукты'

    products = Product.objects.all()  # [:2]
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'products': products,
        'categories': categories,
    }

    return render(request, 'mainapp/products.html', context)
