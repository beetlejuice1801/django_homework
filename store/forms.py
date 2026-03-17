from django import forms
from django.core.exceptions import ValidationError

from store.models import Product


class ProductModelForm(forms.ModelForm):
    """
    Форма для добавления нового продукта.
    """

    class Meta:
        model = Product

        fields = (
            "name",
            "description",
            "price",
        )

        labels = {
            "name": "Название авто",
            "description": "Описание",
            "price": "Цена",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название авто",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите цену",
                }
            ),
        }

    def clean_price(self):
        """
        Метод для валидации цены при добавлении продукта.
        """
        price = self.cleaned_data["price"]
        if price < 3000:
            raise ValidationError(
                message="Цена не может быть ниже 3 000 $",
            )
        return price
