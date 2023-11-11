from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('clothing', views.clothing, name='clothing'),
    path('shoes', views.shoes, name='shoes'),
    path('access', views.access, name='access'),
    path("", views.index),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)