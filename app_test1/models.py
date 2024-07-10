from django.contrib.gis.db import models

class GeoFeature(models.Model):
    name = models.CharField(max_length=100)
    feature_type = models.CharField(max_length=50)
    iso_region = models.CharField(max_length=10)
    feature_id = models.CharField(max_length=20)
    geom = models.PointField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    point = models.PointField()

    def __str__(self):
        return self.name