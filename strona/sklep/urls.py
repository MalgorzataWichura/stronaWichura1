from django.urls import path
from . import views

urlpatterns = [
    path('sklep/', views.sklep, name='sklep'),
    path('kategoria/<str:kategoria>/', views.listaproduktowzkategorii, name='listaproduktowzkategorii'),
    path('kategoria/miesa/<int:id>', views.szczegolymiesa, name='szczegolymiesa'),
    path('kategoria/pieczywo/<int:id>', views.szczegolypieczywa, name='szczegolypieczywa'),
    path('kategoria/napoje/<int:id>', views.szczegolynapoje, name='szczegolynapoje'),
]
