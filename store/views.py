from django.shortcuts import render, get_object_or_404

from store.models import Category, Product


def index(request):
    return render(
        request,
        "store/index.html",
    )


def about(request):
    return render(
        request,
        "store/about.html",
    )


def category_list(request):
    categories = Category.objects.all()
    context = {
        "name": "Список категорий авто",
        "categories": categories,
    }
    return render(
        request,
        "store/category_list.html",
        context,
    )


def product_list(request, category_id):
    category = get_object_or_404(
        Category,
        pk=category_id,
    )
    products = category.products.all()

    context = {
        "name": "Список авто на продажу",
        "products": products,
    }
    return render(
        request,
        "store/product_list.html",
        context,
    )
