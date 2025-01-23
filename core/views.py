from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone
from django.db.models import Count
from django.views.decorators.http import require_http_methods
# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

# Homepage view: Display products and categories

def site_settings(request):
    settings = SiteSettings.objects.first()  # Assumes only one settings instance exists
    return {'site_settings': settings}


def homepage(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})


def services_view(request):
    services = Service.objects.all()  # Fetch all services from the database
    return render(request, 'your_template.html', {'services': services})

def service_details_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_details.html', {'service': service})


def error_400_view(request, exception):
    return render(request, 'home/400.html', status=400)

def error_403_view(request, exception):
    return render(request, 'home/403.html', status=403)

def error_404_view(request, exception):
    return render(request, 'home/404.html', status=404)

def error_500_view(request):
    return render(request, 'home/500.html', status=500)

def error_401_view(request, exception=None):
    return render(request, 'home/401.html', status=401)