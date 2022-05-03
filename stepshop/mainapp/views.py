import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(product):
    same_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return same_products


def products(request, pk=None):
    title = 'продукты'

    links_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        # {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

    products = Product.objects.all()  # .filter(price__gte=500, category__name__endswith='ы').order_by('-price')[:2]
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products == Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'categories': categories,
            'category': category,
            'basket': basket,
        }

        return render(request, 'mainapp/products.html', context)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'categories': categories,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукт'

    links_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        # {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

    # links_menu = ProductCategory.objects.all()
    product_item = get_object_or_404(Product, pk=pk)

    category = product_item.category
    basket = get_basket(request.user)

    same_products = get_same_product(product_item)

    # if not category.is_active or not product_item.is_active:
    #     return HttpResponseRedirect(reverse('products:index'))

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product_item,
        'category': category,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/product.html', context)
