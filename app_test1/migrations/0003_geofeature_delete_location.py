# Generated by Django 5.0.6 on 2024-07-07 07:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test1', '0002_location_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('feature_type', models.CharField(max_length=50)),
                ('iso_region', models.CharField(max_length=10)),
                ('feature_id', models.CharField(max_length=20)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
