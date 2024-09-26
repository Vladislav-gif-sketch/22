from rest_framework import serializers
from .models import MAIN



class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MAIN
        fields = "__all__"