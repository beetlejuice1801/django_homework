from django.contrib import admin

from store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс для регистрации модели Product в админке.
    Attributes:
        list_display: отображаемые поля
        ordering: сортировка по цене
        search_fields: поля для поиска
    """

    list_display = ("name", "description", "price")
    ordering = ("price",)
    search_fields = ("name",)
    search_help_text = "Поиск по названию авто"

    @admin.action(description="Увеличить цену на 100 $")
    def edit_price(self, request, queryset):
        """
        Метод для увеличения цены.
        """
        for product in queryset:
            product.price += 100
            product.save()

    actions = (edit_price,)
