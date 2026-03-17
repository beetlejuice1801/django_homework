"""
Модуль с представлениями.
"""

from django.shortcuts import render, get_object_or_404, redirect

from store.models import Category, Product
from store.forms import ProductModelForm


def index(request):
    """
    Главная страница.
    """
    return render(
        request,
        "store/index.html",
    )


def about(request):
    """
    Страница о нас.
    """
    return render(
        request,
        "store/about.html",
    )


def category_list(request):
    """
    Список существующих категорий.
    :param request: Http-запрос.
    """
    categories = Category.objects.all()
    context = {
        "title": "Список категорий авто",
        "categories": categories,
    }
    return render(
        request,
        "store/category_list.html",
        context,
    )


def product_list(request, category_id):
    """
    Список авто в каждой категории.
    :param category_id: id, по которому продукт
        индентифицируется с категорией.
    """
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    context = {
        "products": products,
        "category": category,
        "category_id": category_id,
    }
    return render(
        request,
        "store/product_list.html",
        context=context,
    )


def product_detail(request, product_id):
    """
    Детальная информация о продукте.
    :param product_id: id, по которому продукт хранится в БД.
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
        "product_id": product_id,
    }
    return render(
        request,
        "store/product_detail.html",
        context=context,
    )


def product_add(request, category_id):
    """
    Представление для добавления продукта через форму ProductModelForm.
    :param category_id: id, по которому продукт
        индентифицируется с категорией.
    """
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.category_id = category_id
            form.save()
            return redirect("category")
    else:
        form = ProductModelForm()

    context = {
        "form": form,
        "title": "Добавить авто",
    }
    return render(
        request,
        "store/product_add.html",
        context=context,
    )


def product_edit(request, product_id):
    """
    Представление для редактирования продукта через форму ProductModelForm.
    :param product_id: id, по которому продукт хранится в БД.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("category")
    else:
        form = ProductModelForm(instance=product)

    context = {
        "form": form,
        "product_id": product_id,
        "title": "Редактировать",
    }
    return render(
        request,
        "store/product_edit.html",
        context=context,
    )
