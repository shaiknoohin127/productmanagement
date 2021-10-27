from django.urls import path
from .views import *
app_name='app'

urlpatterns = [
    path('product_list/',product_list,name='product_list'),
    path('product_details/<int:pk>',product_detail,name='product_details'),
    ]