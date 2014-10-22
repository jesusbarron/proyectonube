from django import forms
from django.forms import ModelForm
from VVehicular.apps.home.models import *
from django.contrib.auth.models import User

#--------------------------------Creando Clase Meta-------------------------
class UserForm(ModelForm):
	class Meta:
		model = userProfile


class VehiculoForm(ModelForm):
	class Meta:
		model = Vehiculo
	def clean_Matricula(self):
		Matricula = self.cleaned_data['Matricula']
		try:
			u = Vehiculo.objects.get(Matricula=Matricula)
		except Vehiculo.DoesNotExist:
				return Matricula
		raise forms.ValidationError('Matricula EXISTENTE')


class ConductorForm(ModelForm):
	class Meta:
		model = Conductor
	def clean_MatriculaV(self):
		MatriculaV = self.cleaned_data['MatriculaV']
		try:
			u = Conductor.objects.get(MatriculaV=MatriculaV)
		except Conductor.DoesNotExist:
				return MatriculaV
		raise forms.ValidationError('Matricula Vehicular EXISTENTE con otro conductor')


class VerificacionForm(ModelForm):
	class Meta:
		model = Verificacion


# -------------Creado manual----------------------------------------------
class contactForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())
	def clean(self):
		return self.cleaned_data

#-------------------Forma de Login UsuarioRoot-----------------------------------
class loginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	def clean(self):
		return self.cleaned_data

class RegisterForm(forms.Form):
	username 	= forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email 		= forms.EmailField(label="Email",widget=forms.TextInput())
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
				return username
		raise forms.ValidationError('Nombre de Usuario EXISTENTE')

	def cleam_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email REGISTRADO')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password NO coinciden')
