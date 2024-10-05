from django.urls import path
from .views import order_view, second_order_view

urlpatterns = [
    path('', order_view, name =''),
    path('list', second_order_view, name='')
]
