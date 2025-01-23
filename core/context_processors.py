from .models import SiteSettings

def site_settings(request):
    settings = SiteSettings.objects.first()  # Assumes only one settings instance exists
    return {'site_settings': settings}
