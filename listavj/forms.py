from django import forms
from .models import *
class agregar_videojuego_form(forms.ModelForm):
	class Meta:
		model= Videojuego 
		fields= '__all__'

class agregar_genero_form(forms.ModelForm):
	class Meta:
		model= Genero 
		fields= '__all__'

class agregar_plataforma_form(forms.ModelForm):
	class Meta:
		model= Plataforma 
		fields= '__all__'

class agregar_desarrollador_form(forms.ModelForm):
	class Meta:
		model= Desarrollador 
		fields= '__all__'

class agregar_distribuidor_form(forms.ModelForm):
	class Meta:
		model= Distribuidor
		fields= '__all__'