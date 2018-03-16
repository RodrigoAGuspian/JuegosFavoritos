from django.urls import path
from .views import *

urlpatterns = [
	path('',vista_index, name='index'),
    path('lista_videojuego/', vista_lista_videojuegos,name= 'videojuego'),
    path('lista_genero/', vista_lista_genero,name= 'genero'),
    path('lista_desarrollador/', vista_lista_desarrollador,name= 'desarrollador'),
    path('lista_distribuidor/', vista_lista_distribuidor,name= 'distribuidor'),
    path('lista_plataforma/', vista_lista_plataforma,name= 'plataforma'),
    path('detalle_videojuego/<int:id_v>/', vista_detalle_videojuegos,name= 'videojuegos_detalle'),
    path('detalle_genero/<int:id_g>/', vista_detalle_genero,name= 'genero_detalle'),
    path('detalle_desarrollador/<int:id_des>/', vista_detalle_desarrollador,name= 'desarrollador_detalle'),
    path('detalle_distribuidor/<int:id_dis>/', vista_detalle_distribuidor,name= 'distribuidor_detalle'),
    path('detalle_plataforma/<int:id_pla>/', vista_detalle_plataforma,name= 'plataforma_detalle'),
    path('agregar_videojuego/', vista_agregar_videojuego,name= 'agregar_videojuego'),
    path('agregar_genero/', vista_agregar_genero,name= 'agregar_genero'),
    path('agregar_desarrollador/', vista_agregar_desarrollador,name= 'agregar_desarrollador'),
    path('agregar_distribuidor/', vista_agregar_distribuidor,name= 'agregar_distribuidor'),
    path('agregar_plataforma/', vista_agregar_plataforma,name= 'agregar_plataforma'),
    
]