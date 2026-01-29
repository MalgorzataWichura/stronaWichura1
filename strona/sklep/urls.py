from django.urls import path
from . import views

urlpatterns = [
    path('sklep/', views.sklep, name='sklep'),
]