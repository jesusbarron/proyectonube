from django.conf.urls.defaults import patterns,url
from VVehicular.apps.home.views import *


urlpatterns = patterns('VVehicular.apps.home.views',

	url(r'^$',index_view.as_view(),name='vista_principal'),
	url(r'^about/$',about_view.as_view(),name='vista_acercade'),
	url(r'^services/$',services_view.as_view(),name='vista_servicios'),
	url(r'^contact/$','contact_view',name='vista_contacto'),
	url(r'^feat/$',features_view.as_view(),name='vista_features'),
	url(r'^ubic/$',ubicaciones_view.as_view(),name='vista_ubicaciones'),
	#---------------------agregar-------------------------------------
	url(r'^addcar/$','addcar_view',name='vista_addcar'),
	url(r'^addcon/$','addcon_view',name='vista_addcon'),
	url(r'^addver/$','addver_view',name='vista_addver'),

	#------------------------URLSBusquedas------------------------------------
	url(r'^buscond/$','buscarconductor_view',name='vista_buscond'),
	url(r'^buscarro/$','buscarcarro_view',name='vista_buscarro'),
	url(r'^busmot/$',buscarmotor_view.as_view(),name='vista_busmot'),
	url(r'^motv4/$','motorv4_view',name='vista_motv4'),
	url(r'^motv6/$','motorv6_view',name='vista_motv6'),
	url(r'^motv8/$','motorv8_view',name='vista_motv8'),
	#-------------------------------------------------------------------------
	
	#-------------------------------urlsPDFS---------------------------------
	url(r'^conpdf/$','conductores_pdf',name='vista_conpdf'),
	url(r'^carrpdf/$','vehiculos_pdf',name='vista_carrpdf'),
	url(r'^veripdf/$','verificacion_pdf',name='vista_veripdf'),

	#-------------------------------URLSGraficas-----------------------------
	url(r'^grafusers/$','estadisticas_view',name='vista_usergraficas'),
	#------------------------------------------------------------------------
	url(r'^register/$','register_view',name='vista_registro'),
	url(r'^adduser/$','adduser_view',name='vista_adduser'),
	#------------------------------------------------------------------------
	url(r'^login/$','signin_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	#-------------------------------URLSTEST-----------------------------------
	#--------------------------------TEST--------------------------------------
	url(r'^test/$',test_view.as_view(),name='vista_test'),
	url(r'^30por/$',trescero_view.as_view(),name='vista_30'),
	url(r'^35por/$',trescinco_view.as_view(),name='vista_35'),
	url(r'^40por/$',cuatrocero_view.as_view(),name='vista_40'),
	url(r'^45por/$',cuatrocinco_view.as_view(),name='vista_45'),
	url(r'^50por/$',cincocero_view.as_view(),name='vista_50'),
	url(r'^60por/$',seiscero_view.as_view(),name='vista_60'),
	url(r'^70por/$',sietecero_view.as_view(),name='vista_70'),
	url(r'^75por/$',sietecinco_view.as_view(),name='vista_75'),
	url(r'^80por/$',ochocero_view.as_view(),name='vista_80'),
	url(r'^85por/$',ochocinco_view.as_view(),name='vista_85'),
	url(r'^90por/$',nuevecero_view.as_view(),name='vista_90'),
	url(r'^95por/$',nuevecinco_view.as_view(),name='vista_95'),
	url(r'^100por/$',cienpor_view.as_view(),name='vista_100'),
)


