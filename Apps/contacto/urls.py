from django.conf.urls import include, url
from . import views


urlpatterns = [
	#url(r'^contacto/', views.contacto,name='contacto'),
        url(r'^contacto/', views.contacto,name='contacto'),
	url('', views.index,name='index'),
	]
