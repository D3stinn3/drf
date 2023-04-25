from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_nyumbani)
    # path('/products', include('products.urls))
]