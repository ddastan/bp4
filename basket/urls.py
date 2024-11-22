from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView, name='order_list'),
    path('create/', views.CreateOrderView, name='order_create'),
    path('update/<int:pk>/', views.UpdateOrderView, name='order_update'),
    path('delete/<int:pk>/', views.DeleteOrderView, name='order_delete'),
]
