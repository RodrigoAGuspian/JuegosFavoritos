from django.db import models

# Create your models here.
class Genero(models.Model):
	
	nombre =models.CharField(max_length= 100)
	descripcion =models.TextField(max_length= 500)
	
	
	def __str__(self):
		return self.nombre

class Desarrollador(models.Model):
	
	nombre =models.CharField(max_length= 100)
	logo=models.ImageField(upload_to='logo', null=True,blank= True)
	
	
	def __str__(self):
		return self.nombre

class Distribuidor(models.Model):
	
	nombre =models.CharField(max_length= 100)
	logo=models.ImageField(upload_to='logo', null=True,blank= True)
	
	
	def __str__(self):
		return self.nombre


class Plataforma(models.Model):
	
	nombre =models.CharField(max_length= 100)
	empresa =models.CharField(max_length= 100)
	imagen_de_la_plataforma=models.ImageField(upload_to='plataformas', null=True,blank= True)
	
	
	def __str__(self):
		return self.nombre

class Videojuego (models.Model):

	nombre=models.CharField(max_length= 100)
	portada=models.ImageField(upload_to='imagen_portada', null=True,blank= True)
	genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
	sub_genero=models.TextField(max_length= 500)
	online=models.BooleanField()
	campana=models.BooleanField()
	fecha_de_salida=models.DateField()
	plataforma=models.ManyToManyField(Plataforma, null= True, blank= True)
	desarrollador=models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
	distribuidor=models.ForeignKey(Distribuidor, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre