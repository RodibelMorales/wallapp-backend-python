from rest_framework import serializers
from wallApp.models import Privacity

class PrivacitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Privacity
        fields=[
            'name',
            'created_at',
            'updated_at',
            'deleted_at'
        ]