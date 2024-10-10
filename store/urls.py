from django.urls import path
from .views import category_list, product_list

urlpatterns = [
    path('product/', product_list, name = 'product_list'),
    path('category/', category_list, name = 'category_list')
]

