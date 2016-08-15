"""foodie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import authenticate, login

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'appfoodie.views.usuario', name='Login'),
    url(r'^listar/$', 'appfoodie.views.listar', name='Inicio'),
    url(r'^listar/listarRes/$', 'appfoodie.views.listarRes'),
    url(r'^listar/listarPro/$', 'appfoodie.views.listarPro'),
    url(r'^listar/listarPed/$', 'appfoodie.views.listarPed'),
    url(r'^listar/listarCli/$', 'appfoodie.views.listarCli'),
    url(r'^listar/listarCli/crear/$', 'appfoodie.views.crear'),
    url(r'^listar/listarRes/crearRes/$', 'appfoodie.views.crearRes'),
    url(r'^listar/listarPro/crearPro/$', 'appfoodie.views.crearPro'),
    url(r'^listar/listarPed/crearPed/$', 'appfoodie.views.crearPed'),
    url(r'^listar/listarCli/modificar/$', 'appfoodie.views.modificar'),
    url(r'^listar/listarRes/modificarRes/$', 'appfoodie.views.modificarRes'),
    url(r'^listar/listarPro/modificarPro/$', 'appfoodie.views.modificarPro'),
    url(r'^listar/listarPed/modificarPed/$', 'appfoodie.views.modificarPed'),
    url(r'^listar/listarCli/eliminar/$', 'appfoodie.views.eliminar'),
    url(r'^listar/listarRes/eliminarRes/$', 'appfoodie.views.eliminarRes'),
    url(r'^listar/listarPro/eliminarPro/$', 'appfoodie.views.eliminarPro'),
    url(r'^listar/listarPed/eliminarPed/$', 'appfoodie.views.eliminarPed'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^list/$', 'appfoodie.views.list'),
    url(r'^listRes/$', 'appfoodie.views.listRes'),
    url(r'^listPro/$', 'appfoodie.views.listPro'),
    url(r'^listPed/$', 'appfoodie.views.listPed'),
    url(r'^listar/Logout/$', 'appfoodie.views.salir', name='Logout'),
    url(r'^gracias/(?P<username>[\w]+)/$', 'appfoodie.views.gracias', name='Gracias'),
    #restframework
    url(r'^productos/$', 'appfoodie.views.survey_list'),
    url(r'^registrar/$', 'appfoodie.views.registrar'),
    url(r'^login/registrar/$', 'appfoodie.views.registrar'),
    url(r'^appfoodie/logout/$', 'appfoodie.views.logout_view'),
    url(r'^gracias/(?P<username>[\w]+)/listar$', 'appfoodie.views.listar'),
   ]