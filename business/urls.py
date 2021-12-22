from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('products', views.product, name="products"),
    path('store', views.store, name="store"),
]
