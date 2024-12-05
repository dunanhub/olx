from django.urls import path
from .views import create_ad, submit_kaspi, delete_ad

# Маршруты для управления объявлениями
urlpatterns = [
    path('create/', create_ad, name='create_ad'),  # Маршрут для создания объявления
    path('kaspi/<int:ad_id>/', submit_kaspi, name='submit_kaspi'),  # Маршрут для оплаты Kaspi
    path('delete/<int:ad_id>/', delete_ad, name='delete_ad'),
]