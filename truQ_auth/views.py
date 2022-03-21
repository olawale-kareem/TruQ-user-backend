from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import permissions
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
import jwt

from .models import User
from .serializers import (SignUpViewSerializer,
                          LoginSerializer, LogoutSerializer)


class SignUpView(generics.GenericAPIView):

    serializer_class = SignUpViewSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class UsersListView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = SignUpViewSerializer(users, many=True)
        return Response(serializer.data)


class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        bearer_token = {'tokens': serializer.data['tokens']}
        return Response(bearer_token, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):

    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutAllUsersView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)
        return Response(status=status.HTTP_204_NO_CONTENT)
