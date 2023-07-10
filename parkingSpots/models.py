from django.db import models

from authenticate.models import CustomUser
from parkingSpots.utils import ParkingSpotStatus, SpotReservationStatus


# Create your models here.
class Spot(models.Model):
    spotLocationName = models.TextField(unique=True)
    latitude = models.TextField()
    longitude = models.TextField()
    status = models.CharField(max_length=200, default=ParkingSpotStatus.ACTIVE.value)
    price = models.FloatField()

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


class ReserveParkingSpot(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, name="reserveUser")
    parkingSpot = models.ForeignKey(Spot, on_delete=models.CASCADE, name="parkingSpot")
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    status = models.CharField(max_length=200, default=SpotReservationStatus.RESERVED.value)
    price = models.FloatField()

    def __str__(self):
        return f"({self.user} spot is {self.startTime} for a time from {self.startTime} to {self.endTime})"
