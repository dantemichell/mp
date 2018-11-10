from django.conf.urls import url, include
from rest_framework import routers
from Apps.usuario import views
from django.contrib import admin
from . import views 
#from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView, LogoutView

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
	url(r'^$', views.index,name='index'),
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^c/', include('Apps.contacto.urls')),
	url(r'^m/', include('Apps.mascotas.urls')),
    url(r'^s/',include('social.apps.django_app.urls',namespace='social2')),
	url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
	url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),

]