from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Bus
from .serializers import BusSerializer
# Create your views here.

class BusView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

