from django.shortcuts import render


def index(request):
    title = "главная страница"

    links_menu = [
        {'href': 'index', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        # {'href': 'about', 'name': 'О&nbsp;нас'},
        {'href': 'contacts', 'name': 'Контакты'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'index.html', context)


def contacts(request):
    return render(request, 'contact.html')
