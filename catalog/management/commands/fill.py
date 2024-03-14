from django.core.management import BaseCommand

from catalog.models import Product, Category
import json


class Command(BaseCommand):


    @staticmethod
    def json_load_categories():
        with open("fixtures/categories.json", 'r', encoding='utf-8') as file:
            content = json.load(file)
        return content

    @staticmethod
    def json_load_products():
        with open("fixtures/products.json", 'r', encoding='utf-8') as file:
            content = json.load(file)
        return content

    def handle(self, *args, **options):
        categories_for_create = []
        product_for_create = []
        Category.objects.all().delete()
        Product.objects.all().delete()
        for category in Command.json_load_categories():
            categories_for_create.append(
                Category(pk=category['pk'],
                         name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(categories_for_create)
        for product in Command.json_load_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'])
            )
        Product.objects.bulk_create(product_for_create)
