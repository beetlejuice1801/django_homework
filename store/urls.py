from django.urls import path
from store.views import (
    index,
    category_list,
    about,
    product_list,
    product_detail,
    product_add,
    product_edit,
)

urlpatterns = [
    path(
        "",
        index,
        name="index",
    ),
    path(
        "about/",
        about,
        name="about",
    ),
    path(
        "category/",
        category_list,
        name="category",
    ),
    path(
        "category/<int:category_id>/products/",
        product_list,
        name="products",
    ),
    path(
        "products/<int:product_id>/detail/",
        product_detail,
        name="product_detail",
    ),
    path(
        "<int:category_id>/add/",
        product_add,
        name="product_add",
    ),
    path(
        "products/<int:product_id>/edit/",
        product_edit,
        name="product_edit",
    ),
]
