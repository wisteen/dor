# Generated by Django 4.2 on 2024-11-28 14:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(max_length=50),
        ),
    ]