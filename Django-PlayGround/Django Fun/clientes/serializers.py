from rest_framework import serializers

from .models import Cliente

from .validators import cpf_valido, celular_valido


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate_cpf(self, cpf):
        if not cpf_valido(cpf):
            raise serializers.ValidationError("CPF precisa de 11 dígitos")
        return cpf

    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("RG precisa ter 9 dígitos.")
        return rg

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Nome não pode ter números.")
        return nome

    def validate_celular(self, celular):
        if not celular_valido(celular):
            raise serializers.ValidationError("Celular está errado")
        return celular
