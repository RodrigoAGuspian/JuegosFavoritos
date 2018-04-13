from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def vista_index (request):

	return render(request, "index.html", locals())


def vista_login(request):
	usuario=""
	clave=""
	if request.method== "POST":
		formulario = Login_form(request.POST)
		if formulario.is_valid():
			usuario= formulario.cleaned_data['usuario']
			clave= formulario.cleaned_data['clave']
			user= authenticate(username=usuario, password=clave)
			if user is not None and user.is_active:
					login(request, user)
					return redirect("/")
			else:
				msj = "usuario o clave incorrecto"

	formulario= Login_form()
	return render (request, "login.html", locals())

def vista_registro(request):
	form=Registro_form()
	if request.method== "POST":
		form=Registro_form(request.POST)
		if form.is_valid():
			usuario= form.cleaned_data['username']
			email= form.cleaned_data['email']
			password1= form.cleaned_data['password_one']
			password_2= form.cleaned_data['password_two']
			if password1==password_2:
				u= User.objects.create_user(username=usuario, email=email, password=password1)
				u.save()
				return render(request, "thanks_for_register.html", locals())
		else:
			return render(request, "registro.html", locals())
	
	return render(request, "registro.html", locals())

def vista_logout(request):
	logout(request)
	return redirect ('index')
			


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

def vista_modificar_videojuego (request, id_v):
	vid= Videojuego.objects.get(id=id_v)
	if request.method=='POST':
		formulario= agregar_videojuego_form(request.POST, request.FILES, instance=vid)
		if formulario.is_valid():
			videojuego=formulario.save(commit=False)
			videojuego.save()
			formulario.save_m2m()
			return redirect('/lista_videojuego/')
	else:
		formulario= agregar_videojuego_form(instance=vid)

	return render(request, 'modificar_videojuego.html',locals())

def vista_eliminar_videojuego (request, id_v):
	ovideojuego= Videojuego.objects.get(id=id_v)
	ovideojuego.delete()
	return redirect("/lista_videojuego/")

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

def vista_modificar_genero (request, id_g):
	gen= Genero.objects.get(id=id_g)
	if request.method=='POST':
		formulario= agregar_genero_form(request.POST, request.FILES, instance=gen)
		if formulario.is_valid():
			genero=formulario.save(commit=False)
			genero.save()
			return redirect('/lista_genero/')
	else:
		formulario= agregar_genero_form(instance=gen)

	return render(request, 'modificar_genero.html',locals())

def vista_eliminar_genero (request, id_g):
	ogenero= Genero.objects.get(id=id_g)
	ogenero.delete()
	return redirect("/lista_genero/")


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
			return redirect('/lista_desarrollador/')
	else:
		formulario= agregar_desarrollador_form()

	return render(request, 'agregar_desarrollador.html',locals())

def vista_modificar_desarrollador (request, id_des):
	des= Desarrollador.objects.get(id=id_des)
	if request.method=='POST':
		formulario= agregar_desarrollador_form(request.POST, request.FILES, instance=des)
		if formulario.is_valid():
			desarrollador=formulario.save(commit=False)
			desarrollador.save()
			return redirect('/lista_desarrollador/')
	else:
		formulario= agregar_desarrollador_form(instance=des)

	return render(request, 'modificar_desarrollador.html',locals())

def vista_eliminar_desarrollador (request, id_des):
	odesarrollador= Desarrollador.objects.get(id=id_des)
	odesarrollador.delete()
	return redirect("/lista_desarrollador/")

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

def vista_modificar_distribuidor (request, id_dis):
	dis= Distribuidor.objects.get(id=id_dis)
	if request.method=='POST':
		formulario= agregar_distribuidor_form(request.POST, request.FILES, instance=dis)
		if formulario.is_valid():
			distribuidor=formulario.save(commit=False)
			distribuidor.save()
			return redirect('/lista_distribuidor/')
	else:
		formulario= agregar_distribuidor_form(instance=dis)

	return render(request, 'modificar_distribuidor.html',locals())

def vista_eliminar_distribuidor (request, id_dis):
	odistribuidor= Distribuidor.objects.get(id=id_dis)
	odistribuidor.delete()
	return redirect("/lista_distribuidor/")

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

def vista_modificar_plataforma (request, id_pla):
	pla= Plataforma.objects.get(id=id_pla)
	if request.method=='POST':
		formulario= agregar_plataforma_form(request.POST, request.FILES, instance=pla)
		if formulario.is_valid():
			plataforma=formulario.save(commit=False)
			plataforma.save()
			return redirect('/lista_plataforma/')
	else:
		formulario= agregar_plataforma_form(instance=pla)

	return render(request, 'modificar_plataforma.html',locals())

def vista_eliminar_plataforma (request, id_pla):
	oplataforma= Plataforma.objects.get(id=id_pla)
	oplataforma.delete()
	return redirect("/lista_plataforma/")