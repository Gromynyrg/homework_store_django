from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)