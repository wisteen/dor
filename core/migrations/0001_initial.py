# Generated by Django 4.2 on 2024-11-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='uploads/projects/')),
                ('description', models.TextField()),
                ('completion_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(help_text="FontAwesome class, e.g., 'fas fa-tools'", max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/services/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default="Do'r Stack Limited", max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/logo/')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='uploads/favicon/')),
                ('email', models.EmailField(default='info@dorstacks.com', max_length=255)),
                ('phone_number', models.CharField(default='+123456789', max_length=20)),
                ('address', models.TextField(default='1234 Construction Lane, Lagos, Nigeria')),
                ('appointment_url', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('twitter', models.URLField(blank=True, max_length=255, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram', models.URLField(blank=True, max_length=255, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('meta_title', models.CharField(default="Welcome to Do'r Stack Limited", max_length=255)),
                ('meta_description', models.TextField(default="Do'r Stack Limited - Delivering exceptional general contracting services with integrity and innovation.")),
                ('meta_keywords', models.TextField(default='general contracting, construction, renovation, cloud services')),
                ('copyright_text', models.CharField(default="© 2024 Do'r Stack Limited. All rights reserved.", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('client_image', models.ImageField(blank=True, null=True, upload_to='uploads/testimonials/')),
                ('testimony', models.TextField()),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
