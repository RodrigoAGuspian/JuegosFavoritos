from django.contrib.auth.models import User
from django import forms
from .models import *
class agregar_videojuego_form(forms.ModelForm):
	campana= forms.BooleanField()
	online= forms.BooleanField()
	

	class Meta:
		model= Videojuego 
		fields= '__all__'
		widgets={
			'fecha_de_salida': forms.TextInput(attrs={'class':'datepicker'}),
			
		}
		exclude= ["campana","online"]

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

class Login_form(forms.Form):
	usuario= forms.CharField(widget=forms.TextInput())
	clave= forms.CharField(widget=forms.PasswordInput(render_value=True))

class Registro_form(forms.Form):
	username 	= forms.CharField(widget=forms.TextInput())
	email 		= forms.EmailField(widget=forms.TextInput())
	password_one 	= forms.CharField(label="Contraseña",widget=forms.PasswordInput(render_value=False))
	password_two	= forms.CharField(label="Confirmar Contrasena",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username= self.cleaned_data['username']
		try:
			u= User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("Este usuario ya existe")

	def clean_email(self):
		email= self.cleaned_data['email']
		try:
			u= User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError("Este email ya existe")

	def clean_password_two(self):
		password_one  = self.cleaned_data["password_one"]
		password_two= self.cleaned_data["password_two"]

		if password_one==password_two:
			pass
		else:
			raise forms.ValidationError("Las contraseñas no coinciden")	
