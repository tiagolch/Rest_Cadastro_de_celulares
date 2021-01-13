from django.contrib import admin
from .models import Telefone


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero', 'modelo', 'setor']
