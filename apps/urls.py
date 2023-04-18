from django.urls import include, path

urlpatterns = [
    path('loja/', include('apps.loja.urls'), name='cadastro-cliente'),
]
