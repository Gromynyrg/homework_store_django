from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
    path('', views.products, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
