from rest_framework import viewsets
from .models import Telefone
from .serializer import TelefoneSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

















