from django import template
from stepshop import settings

register = template.Library()


@register.filter(name='media_folder_products')
def media_folder_products(string):
    if not string:
        string = 'product_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'
