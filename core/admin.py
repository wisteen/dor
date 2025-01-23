from django.contrib import admin
from .models import SiteSettings, Service, Project, Testimonial, ContactMessage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'email', 'phone_number', 'address')

    
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(ContactMessage)
