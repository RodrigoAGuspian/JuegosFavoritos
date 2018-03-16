from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def vista_index (request):

	return render(request, "index.html", locals())

def vista_lista_videojuegos (request):
	lvideojuego= Videojuego.objects.all()

	return render(request, "lista_videojuegos.html", locals())

def vista_detalle_videojuegos (request, id_v):
	datos= Videojuego.objects.get(id=id_v)

	return render(request, "detalle_videojuego.html", locals())

def vista_agregar_videojuego (request):
	if request.method=='POST':
		formulario= agregar_videojuego_form(request.POST, request.FILES)
		if formulario.is_valid():
			videojuego=formulario.save(commit=False)
			videojuego.save()
			formulario.save_m2m()
			return redirect('/lista_videojuego/')
	else:
		formulario= agregar_videojuego_form()

	return render(request, 'agregar_videojuego.html',locals())


def vista_lista_genero (request):
	lgenero= Genero.objects.all()

	return render(request, "lista_genero.html", locals())

def vista_detalle_genero (request, id_g):
	datos= Genero.objects.get(id=id_g)

	return render(request, "detalle_genero.html", locals())

def vista_agregar_genero (request):
	if request.method=='POST':
		formulario= agregar_genero_form(request.POST)
		if formulario.is_valid():
			genero=formulario.save(commit=False)
			genero.save()
			formulario.save_m2m()
			return redirect('/lista_genero/')
	else:
		formulario= agregar_genero_form()

	return render(request, 'agregar_genero.html',locals())


def vista_lista_desarrollador (request):
	ldesarrollador= Desarrollador.objects.all()

	return render(request, "lista_desarrollador.html", locals())

def vista_detalle_desarrollador (request, id_des):
	datos= Desarrollador.objects.get(id=id_des)

	return render(request, "detalle_desarrollador.html", locals())

def vista_agregar_desarrollador (request):
	if request.method=='POST':
		formulario= agregar_desarrollador_form(request.POST, request.FILES)
		if formulario.is_valid():
			desarrollador=formulario.save(commit=False)
			desarrollador.save()
			formulario.save_m2m()
			return redirect('/lista_desarrollador/')
	else:
		formulario= agregar_desarrollador_form()

	return render(request, 'agregar_desarrollador.html',locals())

def vista_lista_distribuidor (request):
	ldistribuidor= Distribuidor.objects.all()

	return render(request, "lista_distribuidor.html", locals())

def vista_detalle_distribuidor (request, id_dis):
	datos= Distribuidor.objects.get(id=id_dis)

	return render(request, "detalle_distribuidor.html", locals())

def vista_agregar_distribuidor (request):
	if request.method=='POST':
		formulario= agregar_distribuidor_form(request.POST, request.FILES)
		if formulario.is_valid():
			distribuidor=formulario.save(commit=False)
			distribuidor.save()
			formulario.save_m2m()
			return redirect('/lista_distribuidor/')
	else:
		formulario= agregar_distribuidor_form()

	return render(request, 'agregar_distribuidor.html',locals())


def vista_lista_plataforma(request):
	lplataforma= Plataforma.objects.all()

	return render(request, "lista_plataforma.html", locals())

def vista_detalle_plataforma (request, id_pla):
	datos= Plataforma.objects.get(id=id_pla)

	return render(request, "detalle_plataforma.html", locals())

def vista_agregar_plataforma (request):
	if request.method=='POST':
		formulario= agregar_plataforma_form(request.POST)
		if formulario.is_valid():
			plataforma=formulario.save(commit=False)
			plataforma.save()
			formulario.save_m2m()
			return redirect('/lista_plataforma/')
	else:
		formulario= agregar_plataforma_form()

	return render(request, 'agregar_plataforma.html',locals())