from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import exceptions
from .utils import get_tokens_for_user
from . import serializers

class UserListView(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        if self.request.user.organization == self.request.tenant:
            qs = get_user_model().objects.filter(organization=self.request.tenant.id)
        else:
            qs = get_user_model().objects.none()
        return qs


class RegisterUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = serializers.RegisterSerializer(request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        tenant = request.tenant
        user = get_user_model()
        email = request.data.get("email")
        password = request.data.get("password")
        response = Response()
        if (email is None) or (password is None):
            raise exceptions.AuthenticationFailed("email and password required")
        user = user.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("user not found")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("wrong password")
        
        if user.organization.id != tenant.id:
            raise exceptions.AuthenticationFailed(f"You don't have an account with {tenant.name}. You have an active account with {user.organization.name}")

        token = get_tokens_for_user(user)
        response.data = token
        return response
