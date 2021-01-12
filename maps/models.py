from django.db import models


class CoordData(models.Model):
    """
    Coordinate data
    """
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
