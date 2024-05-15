from django.db import models
from drones.models import Drone
from django.contrib.auth.models import User

# Create your models here.

class Rental(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.drone} rented by {self.user.username}"
    