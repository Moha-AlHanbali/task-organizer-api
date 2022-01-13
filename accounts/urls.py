
from django.urls import path
from accounts.views import MyObtainTokenPairView, AccountView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', AccountView.as_view(), name='auth_register'),
]