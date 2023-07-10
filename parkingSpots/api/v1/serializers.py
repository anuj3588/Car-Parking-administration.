from rest_framework.serializers import ModelSerializer

from parkingSpots.models import Spot, ReserveParkingSpot


class ParkingSpotSerializer(ModelSerializer):
    class Meta:
        model = Spot
        fields = ["id", "spotLocationName", "latitude", "longitude", "status", "price"]
        read_only_fields = ["id", "status"]


class ReserveParkingSpotSerializer(ModelSerializer):
    class Meta:
        model = ReserveParkingSpot
        fields = ["id", "reserveUser", "parkingSpot", "startTime", "endTime", "status", "price"]
        read_only_fields = ["id", "status"]
