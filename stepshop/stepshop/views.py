from django.shortcuts import render

from mainapp.views import get_hot_product


def index(request):
    title = "главная страница"

    links_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        # {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

    hot_product = get_hot_product()

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
    }

    return render(request, 'index.html', context)


def contacts(request):
    return render(request, 'contact.html')
