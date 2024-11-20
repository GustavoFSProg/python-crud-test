
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.ver_cadastro, name="cadastro"),
    path('home/', views.ver_home, name="home"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('lista/', views.ver_usuario, name="lista"),
# ]
]