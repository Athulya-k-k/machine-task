from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProtectedView,VerifyOTPView,UpdateProfilePictureView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
     path('protected/', ProtectedView.as_view(), name='protected'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
      path('update-profile-picture/', UpdateProfilePictureView.as_view(), name='update_profile_picture'),


]
