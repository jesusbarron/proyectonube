from django.contrib import admin
from VVehicular.apps.home.models import userProfile, Vehiculo,Conductor, Verificacion 

admin.site.register(userProfile)
admin.site.register(Vehiculo)
admin.site.register(Conductor)
admin.site.register(Verificacion)
