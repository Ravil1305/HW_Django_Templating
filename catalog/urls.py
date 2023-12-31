from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, products

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/products/', products, name='products')
]