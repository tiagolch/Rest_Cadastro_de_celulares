from rest_framework import serializers
from tel.models import Telefone


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['numero', 'modelo', 'serial','imei1', 'imei2', 'setor','conta', 'senha', 'mac']

