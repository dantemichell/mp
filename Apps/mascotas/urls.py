from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^adoptar/', views.adopt,name='adoptar'),
	]
