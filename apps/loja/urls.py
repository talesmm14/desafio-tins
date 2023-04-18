from django.urls import path
from apps.loja import views

urlpatterns = [
    path('cliente/add/', views.cadastro_cliente, name='cadastro-cliente'),
]
