from django.urls import path
from . import views
from .views import DeviceListView, DeviceDetailView

urlpatterns = [
    path('', DeviceListView.as_view()),
    path('<int:pk>/', DeviceDetailView.as_view()),
]