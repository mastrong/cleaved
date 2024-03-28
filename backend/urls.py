from django.urls import path
from . import views

urlpatterns = [
    path('appetizers/', views.get_appetizer, name='appetizers'),
    path('entrees/', views.get_entree, name='entrees'),
    path('desserts/', views.get_dessert, name='desserts'),
]
