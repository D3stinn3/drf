from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ProductList.as_view()),
    # path('', views.ProductCreate.as_view()),
    path('', views.productView ),
    path('<int:pk>/', views.productView),
    path('<int:pk>/update', views.ProductUpdate.as_view()),
    path('<int:pk>/delete', views.ProductDelete.as_view()),
    path('view/', views.ProductMixin.as_view()),
    path('<str:pk>/mixin', views.ProductMixin.as_view()),
    path('<str:pk>/details', views.ProductDetail.as_view())
    # path('<int:pk>/destroy')
]