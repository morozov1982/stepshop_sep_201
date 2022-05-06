import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def products(request, pk=None, page=1):
    title = 'продукты'

    links_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        # {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

    products = Product.objects.filter(is_deleted=False)
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)
    category = {'name': 'все'}

    if pk is not None:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(is_deleted=False, category__pk=pk).order_by('price')

        if category.is_deleted:
            return HttpResponseRedirect(reverse('products:index'))

    paginator = Paginator(products, 3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products_paginator,  # 'products': products,
        'categories': categories,
        'pk': pk,
        'category': category,
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
