from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('manas_list/', views.ManasListView.as_view(), name='manas_list'),
    path('manas_parser/', views.ManasFormView.as_view(), name='manas_parser'),
]