from django.urls import path
from core.views import product_view

urlpatterns = [
    path('core/', product_view.product_list, name='product_list'),
    path('core/create/', product_view.product_create, name='product_create'),
]
