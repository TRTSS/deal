from rest_framework import serializers

from storage.models import StorageUnit


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageUnit
        fields = '__all__'
