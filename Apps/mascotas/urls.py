from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        url(r'^adoptar/', views.adopt,name='adoptar'),
		url(r'^galeria/', views.galeria,name='galeria'),
	] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)