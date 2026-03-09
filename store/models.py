"""
Определяем базовые модели.
"""

from django.db import models


class Product(models.Model):
    """Класс для описания в каком виде храним данные продукта в БД.
    Attributes:
        name: Название продукта
        description: Описание
        price: Цена
        created_at: Время создания записи
        category: Связь продуктов с категорией через ForeignKey
        (в одной категории может быть несколько продуктов)

    """

    name = models.CharField(
        max_length=40,
        unique=True,
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Category(models.Model):
    """Класс для описания в каком виде храним все категории продуктов в БД.
    Attributes:
        name: Название категории
        description: Описание

    """

    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
