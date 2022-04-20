import json
import os.path

from django.core import management
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('flush', verbosity=0, interactive=False)

        categories = load_from_json('categories')
        products = load_from_json('products')

        # ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        # Product.objects.all().delete()

        for product in products:
            category_pk = product['category']
            _category = ProductCategory.objects.get(pk=category_pk)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.create_superuser('admin', 'admin@admin.com', '123', age=30)
