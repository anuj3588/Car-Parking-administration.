from datetime import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from parkingSpots.api.coordinates import calculate_coordinates_within_radius
from parkingSpots.api.v1.serializers import ParkingSpotSerializer, ReserveParkingSpotSerializer
from parkingSpots.models import Spot, ReserveParkingSpot
from parkingSpots.utils import DateFormat

RADIUS = 1000


# Create your views here.
class ParkingViews(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        search = request.GET.get('search', "False") == "True"
        if search:
            latitude = float(request.GET.get('latitude'))
            longitude = float(request.GET.get('longitude'))
            radius = float(request.GET.get('radius', RADIUS))
            if not latitude or not longitude:
                raise Exception("latitude and longitude are required parameters")
            allCoordinates = calculate_coordinates_within_radius(latitude, longitude, radius)

            # Create a list of Q objects for each latitude-longitude pair
            q_objects = [Q(latitude__icontains=(lat), longitude__icontains=str(lon)) for lat, lon in allCoordinates]
            # Combine the Q objects using the OR operator
            filter_query = Q()
            for q_object in q_objects:
                filter_query |= q_object

            instance = Spot.objects.filter(filter_query)

        else:
            instance = Spot.objects.all()
        serializer = ParkingSpotSerializer(instance, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        payload = request.data
        serializer = ParkingSpotSerializer(data=payload)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        request.POST._mutable = True
        return Response({"data": "New spot added successfully"}, status=status.HTTP_201_CREATED)


class ReserveSpotViews(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        instance = request.user
        reservedSpots = ReserveParkingSpot.objects.filter(reserveUser_id=instance.id).all()
        serializer = ReserveParkingSpotSerializer(reservedSpots, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        """
        Required Validations need to add in future
            Check if same spot is already booked for same time frame for the same day
        :param request:
        :return:
        """
        loggedInUser = request.user
        payload = request.data
        payload["reserveUser"] = loggedInUser.id
        # Calculate parking price
        parkingSpot = Spot.objects.filter(id=payload['parkingSpot']).first()
        startTime = datetime.strptime(payload['startTime'], DateFormat.DATETIMEFORMAT.value)
        endTime = datetime.strptime(payload['endTime'], DateFormat.DATETIMEFORMAT.value)
        difference = endTime - startTime

        hours = difference.days * 24 + difference.seconds // 3600
        payload['price'] = hours * parkingSpot.price

        serializer = ReserveParkingSpotSerializer(data=payload)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        request.POST._mutable = True
        serializer.save()
        return Response({"data": "Spot reserved successfully"}, status=status.HTTP_201_CREATED)


class ReserveSpotPriceViews(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, spotName, hours):
        parkingSpot = Spot.objects.filter(spotLocationName=spotName).first()
        price = hours * parkingSpot.price
        return Response({"price": price})
