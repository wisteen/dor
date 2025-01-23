from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

from django.utils import timezone
from .constants import *
from django.utils.text import slugify


from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings


class SiteSettings(models.Model):
    # Basic Website Details
    site_name = models.CharField(max_length=200, default="Do'r Stack Limited")
    logo = models.ImageField(upload_to='uploads/logo/', null=True, blank=True)
    favicon = models.ImageField(upload_to='uploads/favicon/', null=True, blank=True)
    email = models.EmailField(max_length=255, default="info@dorstacks.com")
    phone_number = models.CharField(max_length=20, default="+123456789")
    address = models.TextField(default="1234 Construction Lane, Lagos, Nigeria")
    appointment_url = models.URLField(blank=True, null=True)

    # Social Media Links
    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    youtube_url = models.URLField(blank=True, null=True)

    # SEO and Metadata
    meta_title = models.CharField(max_length=255, default="Welcome to Do'r Stack Limited")
    meta_description = models.TextField(
        default="Do'r Stack Limited - Delivering exceptional general contracting services with integrity and innovation."
    )
    meta_keywords = models.TextField(default="general contracting, construction, renovation, cloud services")

    # Footer Section
    copyright_text = models.CharField(max_length=255, default="© 2024 Do'r Stack Limited. All rights reserved.")

    def __str__(self):
        return self.site_name

class Service(models.Model):
    # Services offered by the company
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="FontAwesome class, e.g., 'fas fa-tools'")
    image = models.ImageField(upload_to='uploads/services/', null=True, blank=True)
    description = models.TextField(max_length=50)
    slug = models.SlugField(unique=True)
    content = RichTextField()


    def __str__(self):
        return self.name

class Project(models.Model):
    # Projects to showcase on the website
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/projects/')
    description = models.TextField()
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    # Client Testimonials
    client_name = models.CharField(max_length=200)
    client_image = models.ImageField(upload_to='uploads/testimonials/', null=True, blank=True)
    testimony = models.TextField()
    position = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.client_name

class ContactMessage(models.Model):
    # Messages submitted through the contact form
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

