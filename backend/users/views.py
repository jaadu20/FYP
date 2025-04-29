import random
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_str
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CandidateProfile, PasswordReset
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import (
    SignupSerializer,
    MyTokenObtainPairSerializer,
    ForgotPasswordSerializer,

)
User = get_user_model()

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny] 


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this email does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        code = str(random.randint(100000, 999999))
        PasswordReset.objects.create(user=user, code=code)

        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        send_mail(
        "Password Reset Request",
        f"Your password reset code is: {code}\n\n"
        f"Or reset your password using the link below:\n"
        f"http://localhost:5174/resetpassword/{uidb64}/{token}",
        "x@gmail.com",  
        [email],
        fail_silently=False,
    )

        return Response(
            {"detail": "Password reset email sent! Check your inbox."},
            status=status.HTTP_200_OK,
        )

