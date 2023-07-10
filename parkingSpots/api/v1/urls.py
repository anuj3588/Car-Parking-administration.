from django.urls import path

from parkingSpots.api.v1.views import ParkingViews, ReserveSpotViews, ReserveSpotPriceViews

urlpatterns = [
    path("spot", ParkingViews.as_view(), name="spot"),
    path("book/spot", ReserveSpotViews.as_view(), name="spot"),
    path("book/spot/price/<str:spotName>/<int:hours>", ReserveSpotPriceViews.as_view(), name="spot"),
]
