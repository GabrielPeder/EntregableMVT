
from django.contrib import admin
from django.urls import path
from Familiares.views import index
from miembros.views import listadoMiembros,addMember

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('listadoMiembros/', listadoMiembros),
    path('agregarMiembro/', addMember),
]
