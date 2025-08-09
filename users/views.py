from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .utils import generate_otp, send_otp_email
from .models import EmailOTP, User
from rest_framework.parsers import MultiPartParser, FormParser


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'You are authenticated!'}, status=200)


class RegisterView(APIView):
    def get(self, request):
        return Response({"message": "Please send a POST request to register."}, status=200)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            otp = generate_otp()
            EmailOTP.objects.create(user=user, otp=otp)
            send_otp_email(user.email, otp)

            return Response({'message': 'User registered. OTP sent to email.'}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)


        if user:
            if not user.is_active:
                return Response({'error': 'Email not verified'}, status=403)

            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        return Response({'error': 'Invalid credentials'}, status=400)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=205)
        except Exception as e:
            return Response(status=400)



class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        try:
            user = User.objects.get(email=email)
            otp_obj = EmailOTP.objects.get(user=user)

            if otp_obj.is_expired():
                return Response({'error': 'OTP expired'}, status=400)

            if otp_obj.attempts >= 5:
                return Response({'error': 'Too many attempts'}, status=403)

            if otp_obj.otp == otp:
                user.is_active = True
                user.save()
                otp_obj.delete()
                return Response({'message': 'Email verified successfully'}, status=200)
            else:
                otp_obj.attempts += 1
                otp_obj.save()
                return Response({'error': 'Invalid OTP'}, status=400)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        except EmailOTP.DoesNotExist:
            return Response({'error': 'OTP not found'}, status=404)



class UpdateProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request):
        user = request.user
        profile_pic = request.data.get('profile_picture')
        if not profile_pic:
            return Response({'error': 'No file uploaded'}, status=400)

        user.profile_picture = profile_pic
        user.save()
        return Response({'message': 'Profile picture updated successfully'})