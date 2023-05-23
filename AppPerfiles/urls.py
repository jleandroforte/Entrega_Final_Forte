
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from AppPerfiles.views import *


urlpatterns = [
  
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('editar_perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('editar_avatar/', agregar_avatar, name="editar_avatar"),
    
]


