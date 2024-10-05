from django.urls import path
from .views import store_view, second_store_view

urlpatterns = [
    path('', store_view, name = 'store_main'),
    path('specific', second_store_view, name = 'store_specific')
]