from django.db import models


class Telefone(models.Model):
    numero = models.CharField(max_length=11)
    modelo = models.CharField(max_length=20)
    serial = models.CharField(max_length=30)
    imei1 = models.CharField(max_length=20)
    imei2 = models.CharField(max_length=20, null=True, blank=True)
    setor = models.CharField(max_length=20)
    conta = models.EmailField()
    senha = models.CharField(max_length=15)
    mac = models.CharField(max_length=17)

    def __str__(self):
        return self.numero


