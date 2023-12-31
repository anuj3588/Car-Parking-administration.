from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authenticate.views import RegisterView, EmailTokenObtainPairView

urlpatterns = [
    path('register', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/obtain', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
