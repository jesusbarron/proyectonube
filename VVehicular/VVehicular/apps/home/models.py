from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#----------------------Usuario root------------------------------------------

class userProfile(models.Model):
	user=models.OneToOneField(User)
	phone=models.CharField(max_length=15)
	def __unicode__(self):
		return self.user.username

#------------------MODELOS PROYECTO-------------------------
Proc_Choices=(('Fronterizo','Fronterizo'),('Nacional','Nacional'),('Nacionalizado','Nacionalizado'))
Clas_Choices=(('Automovil','Automovil'),('Camion','Camion'),('Motocicleta','Motocicleta'),('Otros','Otros'))
Motor_Choices=(('V4','V4'),('V6','V6'),('V8','V8'))

class Vehiculo(models.Model):
	Matricula			= models.CharField(max_length=9)
	Procedencia			= models.CharField(max_length=30,choices=Proc_Choices)
	NoSerie				= models.CharField(max_length=15)
	Marca 				= models.CharField(max_length=50)
	Color				= models.CharField(max_length=20)
	Clase 				= models.CharField(max_length=30,choices=Clas_Choices)
	Capacidad 			= models.IntegerField()
	Year				= models.IntegerField()
	Puertas				= models.IntegerField()
	Motor				= models.CharField(max_length=10,choices=Motor_Choices)
	status				= models.BooleanField(default=True)
	date_joined			= models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.Matricula

class Conductor(models.Model):
	NoLicencia			= models.CharField(max_length=15)
	MatriculaV			= models.ForeignKey(Vehiculo)
	Nombre 				= models.CharField(max_length=50)
	ApellidoPaterno		= models.CharField(max_length=50)
	ApellidoMaterno 	= models.CharField(max_length=50)
	Direccion 			= models.CharField(max_length=200)
	Telefono			= models.CharField(max_length=15)
	status				= models.BooleanField(default=True)
	def  __unicode__(self):
		return self.NoLicencia

class Verificacion(models.Model):
	Empleado 			= models.ForeignKey(userProfile)
	ConductorV			= models.ForeignKey(Conductor)
	ConsumoGasolina		= models.CharField(max_length=50)
	EmisionSmog			= models.CharField(max_length=50)
	Fecha 				= models.DateTimeField(auto_now_add=True)
	status				= models.BooleanField(default=True)
	def  __unicode__(self):
		return self.Folio



		



