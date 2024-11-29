from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.CreateOrderView.as_view(), name='order_create'),
    path('update/<int:pk>/', views.UpdateOrderView.as_view(), name='order_update'),
    path('delete/<int:pk>/', views.DeleteOrderView.as_view(), name='order_delete'),
]
