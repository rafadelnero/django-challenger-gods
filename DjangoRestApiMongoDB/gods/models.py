from django.db import models


class God(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    power = models.CharField(max_length=200, blank=False, default='')
    greek = models.BooleanField(default=False)
