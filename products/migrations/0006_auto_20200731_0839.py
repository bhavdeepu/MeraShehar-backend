# Generated by Django 3.0.8 on 2020-07-31 08:39

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='images',
            new_name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=products.models.get_image_filename),
        ),
    ]