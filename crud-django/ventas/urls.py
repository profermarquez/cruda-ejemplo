from django.urls import path
from . import views

urlpatterns = [
    path('', views.venta_list, name='venta_list'),
    path('create/', views.venta_create, name='venta_create'),
    path('update/<int:id>/', views.venta_update, name='venta_update'),
    path('delete/<int:id>/', views.venta_delete, name='venta_delete'),
]

