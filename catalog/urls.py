from django.urls import path
from catalog.views import (
    ProductListView,
    CategoriesListView,
    OrdersTemplateView,
    ContactsTemplateView,
    ProductDetailView,
    ProductCreateView
)

# исключаем одноименные конфликты
app_name = 'catalog'

urlpatterns = [
    # маршрут для домашней страницы 1
    path('', ProductListView.as_view(), name='21-2_home1'),

    # маршрут для Категорий страница 2
    path('categories/', CategoriesListView.as_view(), name='21-2_home2'),

    # маршрут для Заказов страница 3
    path('orders/', OrdersTemplateView.as_view(), name='21-2_home3'),

    # маршрут для страницы 4 контактов с закрывающим /
    path('contacts/', ContactsTemplateView.as_view(), name='21-2_home4'),

    # -24-Задание 1
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Маршрут для создания товара
    path('products/create/', ProductCreateView.as_view(), name='create_product'),
]
