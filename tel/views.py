from rest_framework import viewsets
from .models import Telefone
from .serializer import TelefoneSerializer


class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer













