# Generated by Django 3.0.8 on 2020-07-29 18:36

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='default.png', upload_to=products.models.get_image_filename)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
