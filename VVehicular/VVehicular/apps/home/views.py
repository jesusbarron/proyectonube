#------------------para generar PDF!!--------------------
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
from django.http import HttpResponse
#--------------------------------------
#------------------------Generar Graficas--------------------------
import datetime
import qsstats
#------------------------------------------------------------------
from django.shortcuts import render_to_response
from django.template import RequestContext
from VVehicular.apps.home.forms import *
from django.http import HttpResponseRedirect
#-----------------------------------------------------------------
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#-----------------para busquedas-------------------------------
from VVehicular.apps.home.models import Vehiculo, Conductor, Verificacion
#----------------------------Vista genericas------------------------
from django.views.generic import TemplateView, CreateView
#from demo.apps.home.models import cliente
from django.core.urlresolvers import reverse_lazy
#-------------------Generar consultas avanzadas-----------------
from django.db.models import Q


# Create your views here.


#-------Usando clases-----------------------------------------------------
class index_view(TemplateView):
	template_name='home/index.html'

class about_view(TemplateView):
	template_name='home/about-us.html'	

class services_view(TemplateView):
	template_name='home/services.html'	

class features_view(TemplateView):
	template_name='home/features.html'	

class ubicaciones_view(TemplateView):
	template_name='home/ubicacion.html'	

class buscarmotor_view(TemplateView):
	template_name='home/buscmotor.html'		

#-------------------------------vista para el login--------------------------------------
def signin_view(request):
	mensaje=''
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			form = loginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = 'Usuario y/o password incorrectos'

		form = loginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/sign-in.html',ctx,context_instance=RequestContext(request))

#------------------------------------LogOut-------------------------------------------
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

#----------------------------------Registrar-------------------------------------------
@login_required(login_url='/login')
def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() #guardamos el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/sign-up.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/sign-up.html',ctx,context_instance=RequestContext(request))

#---------------------------------------------------------------------------------------------------------

def adduser_view(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('#')
	else:
		form=UserForm()
	return render_to_response('home/adduser.html',{'form':form}, context_instance=RequestContext(request))


def addcar_view(request):
	if request.method=='POST':
		form=VehiculoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('#')
	else:
		form=VehiculoForm()
	return render_to_response('home/addcar.html',{'form':form}, context_instance=RequestContext(request))


def addcon_view(request):
	if request.method=='POST':
		form=ConductorForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('#')
	else:
		form=ConductorForm()
	return render_to_response('home/addcon.html',{'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def addver_view(request):
	if request.method=='POST':
		form=VerificacionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('#')
	else:
		form=VerificacionForm()
	return render_to_response('home/addver.html',{'form':form}, context_instance=RequestContext(request))

#---------------------modelosMANUAL---------------------------------------


def contact_view(request):
	form = contactForm()
	ctx = {'form':form}
	return render_to_response('home/contact.html',ctx,context_instance=RequestContext(request))

#-------------------------------Busquedas---------------------------------------------
def buscarconductor_view(request):
	query = request.GET.get('q','')
	if query:
		qset = (Q(NoLicencia=query))
		results = Conductor.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('home/buscarconductor.html',{"results":results,"query":query})

def buscarcarro_view(request):
	query = request.GET.get('q','')
	if query:
		qset = (Q(Matricula=query))
		results = Vehiculo.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('home/buscarcarro.html',{"results":results,"query":query})



	

#----------------------Vista para Graficas-----------------------------
@login_required(login_url='/login')
def estadisticas_view(request):
    GOOGLE_API_KEY = 'AIzaSyAE0R4Rty0NlPzrF_7qEUWRU4-1CoQNvE4'
    qs = Vehiculo.objects.all()
    qss = qsstats.QuerySetStats(qs, 'date_joined')
    hoy = datetime.date.today()
    hace_2_semanas = hoy - datetime.timedelta(days=2)
    users_stats = qss.time_series(hace_2_semanas, hoy)
    return render_to_response('home/estadisticas.html',locals(),context_instance=RequestContext(request))

#----------------------Generar Reporte-----------------------------------------------
def generar_pdf(html):
	#funcion para generar el archivo PDF y devolverlo por HttpResponse
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),mimetype='application/pdf')
	return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def conductores_pdf(request):
	conduc =Conductor.objects.order_by('NoLicencia')
	ctx = {'pagesize':'A4','conduc':conduc}
	html = render_to_string('home/pdftodocond.html',ctx,context_instance=RequestContext(request))
	return generar_pdf(html)

def vehiculos_pdf(request):
	veh =Vehiculo.objects.order_by('Matricula','NoSerie','Marca')
	ctx = {'pagesize':'A4','veh':veh}
	html = render_to_string('home/carrospdftodo.html',ctx,context_instance=RequestContext(request))
	return generar_pdf(html)

def verificacion_pdf(request):
	veri =Verificacion.objects.order_by('id','Fecha')
	ctx = {'pagesize':'A4','veri':veri}
	html = render_to_string('home/verpdf.html',ctx,context_instance=RequestContext(request))
	return generar_pdf(html)

#----------------------------BUsquedas MotorPDF-------------------------------------
def motorv4_view(request):
	veh =Vehiculo.objects.filter(Motor="V4")
	ctx = {'pagesize':'A4','veh':veh}
	html = render_to_string('home/motorv4.html',ctx,context_instance=RequestContext(request))
	return generar_pdf(html)

def motorv6_view(request):
	veh =Vehiculo.objects.filter(Motor="V6")
	ctx = {'pagesize':'A4','veh':veh}
	html = render_to_string('home/motorv6.html',ctx,context_instance=RequestContext(request))
	return generar_pdf(html)

def motorv8_view(request):
	veh =Vehiculo.objects.filter(Motor="V8")
	ctx = {'pagesize':'A4','veh':veh}
	html = render_to_string('home/motorv8.html',ctx,context_instance=RequestContext(request))
	return generar_pdf(html)


#---------------------------------TEST-----------------------------------------------
class test_view(TemplateView):
	template_name='home/test.html'

class trescero_view(TemplateView):
	template_name='home/30por.html'

class trescinco_view(TemplateView):
	template_name='home/35por.html'

class cuatrocero_view(TemplateView):
	template_name='home/40por.html'

class cuatrocinco_view(TemplateView):
	template_name='home/45por.html'

class cincocero_view(TemplateView):
	template_name='home/50por.html'

class seiscero_view(TemplateView):
	template_name='home/60por.html'

class sietecero_view(TemplateView):
	template_name='home/70por.html'

class sietecinco_view(TemplateView):
	template_name='home/75por.html'

class ochocero_view(TemplateView):
	template_name='home/80por.html'

class ochocinco_view(TemplateView):
	template_name='home/85por.html'

class nuevecero_view(TemplateView):
	template_name='home/90por.html'

class nuevecinco_view(TemplateView):
	template_name='home/95por.html'

class cienpor_view(TemplateView):
	template_name='home/100por.html'
#---------------------------