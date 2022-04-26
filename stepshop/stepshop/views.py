from django.shortcuts import render


def index(request):
    title = "главная страница"

    links_menu = [
        {'href': 'index', 'name': 'Главная', 'route': ''},
        {'href': 'products:index', 'name': 'Продукты', 'route': 'products/'},
        # {'href': 'about', 'name': 'О&nbsp;нас', 'route': 'about/'},
        {'href': 'contacts', 'name': 'Контакты', 'route': 'contacts/'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'index.html', context)


def contacts(request):
    return render(request, 'contact.html')
