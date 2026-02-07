from django.urls import path
from . import views

urlpatterns = [
    path('sklep/', views.sklep, name='sklep'),
    path('kategoria/<str:kategoria>/', views.listaproduktowzkategorii, name='listaproduktowzkategorii'),
    path('kategoria/miesa/<int:id>', views.szczegolymiesa, name='szczegolymiesa'),
    path('kategoria/pieczywo/<int:id>', views.szczegolypieczywa, name='szczegolypieczywa'),
    path('kategoria/napoje/<int:id>', views.szczegolynapoje, name='szczegolynapoje'),
    path('kategoria/owoce/<int:id>', views.szczegolyowoce, name='szczegolyowoce'),
    path('kategoria/warzywa/<int:id>', views.szczegolywarzywa, name='szczegolywarzywa'),
    path('koszyk/', views.pokaz_koszyk, name='pokaz_koszyk'),
    path('koszyk/dodaj/<str:kategoria>/<int:id>/', views.dodaj_do_koszyka, name='dodaj_do_koszyka'),
    path('koszyk/usun/<str:klucz>/', views.usun_z_koszyka, name='usun_z_koszyka'),
]