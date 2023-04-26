from rest_framework import serializers
from .models import Client, Domain

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name"]


    def create(self, validated_data):
        name = validated_data["name"]
        tenant = Client(schema_name=name, name=name)
        tenant.save()
        domain = Domain()
        domain.domain = f'{name}.metro.local'
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()
        return tenant
