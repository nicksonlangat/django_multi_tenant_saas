from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Client
from .serializers import ClientSerializer
# Create your views here.

class ClientView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
