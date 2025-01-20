from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "products/", include("products.urls", namespace="products")
    ),  # маршрут к приложению Товары
    path(
        "nodes/", include("nodes.urls", namespace="nodes")
    ),  # маршрут к приложению Объекты сети
    path(
        "users/", include("users.urls", namespace="users")
    ),  # маршрут к приложению Пользователей
]
