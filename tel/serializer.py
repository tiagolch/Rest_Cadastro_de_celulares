from rest_framework import serializers
from tel.models import Telefone


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['id','numero', 'modelo', 'serial','imei1', 'imei2', 'setor','conta', 'senha', 'mac']

    def validate_mac(self, mac):
        if len(mac) != 17:
            raise serializers.ValidationError("O Campo 'Mac' deve ter 17 caracteres")
        return mac
