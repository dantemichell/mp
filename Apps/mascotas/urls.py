from django.conf.urls import include, url
from . import views




urlpatterns = [
        url(r'^adoptar/', views.adopt,name='adoptar'),
		url(r'^galeria/', views.galeria,name='galeria'),
		url(r'^gracias/', views.gracias,name='gracias'),
		url(r'^perrito/(?P<id>[0-9]+)/$', views.adoptar,name='adoptarperrito'),
	] 

