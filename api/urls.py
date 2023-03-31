from django.urls import path
from api.views import EmpresaView


urlpatterns = [
    path('empresas/',EmpresaView.as_view(), name='empresas'),
    path('empresas/<int:id>',EmpresaView.as_view(), name='empresas_procesos'),
    ]