# Generated by Django 3.0.8 on 2020-07-29 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='items',
            new_name='product',
        ),
    ]
