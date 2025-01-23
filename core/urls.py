from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as form_validation
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('services/', views.services_view, name='services'),
    path('service/<slug:slug>/', views.service_details_view, name='service_details'), 
]


