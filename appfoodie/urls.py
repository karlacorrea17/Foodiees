from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'appfoodie.views.listar'),
	url(r'^listarRes/$', 'appfoodie.views.listarRes'),
	url(r'^crear/$', 'appfoodie.views.crear'),
	url(r'^modificar/$', 'appfoodie.views.modificar'),
]