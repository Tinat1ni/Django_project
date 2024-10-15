from django.urls import path
from .views import category_list, category_products, product_details

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('category/<int:category_id>/products/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_details, name='product_details'),

]

