"""
Генерация тестовых данных для записей в БД.
"""

from django.core.management.base import BaseCommand
from store.models import Product, Category
import random
from faker import Faker
from faker_vehicle import VehicleProvider


class Command(BaseCommand):
    """Кастомная команда для генерации тестовых данных в таблицах."""

    help = "Генерация тестовых данных"

    def handle(self, *args, **options):
        self.stdout.write("Запущена генерация")

        fake = Faker()
        fake.add_provider(VehicleProvider)

        # Генерируем категории с помощью функции range и экземпляра класса Faker().
        categories = []
        for i in range(2):
            category = Category.objects.create(
                name=fake.vehicle_make(),
                description=fake.text(max_nb_chars=70),
            )
            categories.append(category)

        # Генерируем продукты с помощью функции range и экземпляра класса Faker().
        products = []
        for i in range(13):
            product = Product.objects.create(
                name=fake.vehicle_model(),
                description=fake.text(max_nb_chars=200),
                price=fake.pyfloat(
                    min_value=3000,
                    max_value=20000,
                    right_digits=2,
                ),
                category=random.choice(categories),
            )
            products.append(product)
        self.stdout.write("Заверешена генерация")
