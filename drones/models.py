from django.db import models
from django.contrib.auth.models import User

class Drone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.brand} {self.model}"




