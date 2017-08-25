from django.conf.urls import url
from django.contrib import *
from adi.views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', inicio),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name="login_p"),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name="logout_p"),
    url(r'^preceptor/$', preceptor, name="cambio"),
    url(r'^guardia/$', guardia, name="cambio2"),
    url(r'^alumno/$', alumno, name="cambio3"),
    url(r'^crearpreceptor/$', cpreceptor, name="cambio4"),
    url(r'^crearalumno/$', calumno, name="cambio5"),
    url(r'^cambiaralumno/$', chalumno, name="cambio6"),
    url(r'^f2/$', f2, name="f2"),
    url(r'^crearf2/$', crear_formulario2, name="crear_formulario2"),
    url(r'^crearf3/$', crear_formulario3, name="crear_formulario3"),
    url(r'^crearal/$', crear_alumno, name="crear_alumno"),
    url(r'^formularios/$', formularios, name="formularios"),
    url(r'^guardia_f2/$', f2s, name="f2s"),
    url(r'^alumnos/$', alumnos, name="f2grupal"),
    url(r'^mis_alumnos/$', mis_alumnos, name="mis_alumnos"),
    url(r'^modal/$', modificar_alumno, name="modificar_alumno"),
    url(r'^presente/(\d+)$', presente, name="presente"),
    url(r'^retiro/(\d+)$', retiro_grupal, name="retiro_grupal"),
    url(r'^guardia_aceptar/(\d+)$', aceptar, name="aceptar"),
    url(r'^pepe/(\d+)$', pepe, name="pepe"),
    url(r'^datos_f2/(\d+)$', datos_f2, name="datos_f2"),
    url(r'^datos_f3/(\d+)$', datos_f3, name="datos_f3"),
    url(r'^volver/(\d+)$', volver, name="volver"),
    url(r'^busal/$', buscar_alumno, name="buscar_alumno")
]
