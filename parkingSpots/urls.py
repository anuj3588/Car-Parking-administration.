from django.urls import path, include


urlpatterns = [
    path("api/v1/", include('parkingSpots.api.v1.urls')),
]
