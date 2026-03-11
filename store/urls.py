from django.urls import path
from store.views import index, category_list, product_list, about

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("category/", category_list, name="category"),
    path("category/<int:category_id>/", product_list, name="product"),
]
