from rest_framework.viewsets import ModelViewSet
from .models import Hall, Client
from .serializers import HallSerializer, ClientSerializer


class HallModelViewSet(ModelViewSet):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class ClientModelViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
