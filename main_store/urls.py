from django.urls import path, include
from . import views


app_name = 'main_store'

urlpatterns = [
    path('', views.product_all, name='store_home'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
