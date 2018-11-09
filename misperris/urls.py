from django.conf.urls import url, include
from rest_framework import routers
from Apps.usuario import views
from django.contrib import admin
from . import views

'''
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
'''
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
#    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'', include('Apps.contacto.urls')),
	url(r'', include('Apps.mascotas.urls')),
    url('',include('social.apps.django_app.urls',namespace='social')),
    url(r'^salir/$', views.logOut, name='logOut'),

]