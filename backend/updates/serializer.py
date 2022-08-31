from dataclasses import fields
from rest_framework import serializers
from .models import Updates

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updates
        fields = ['title','slug','cover','content','created','downloads']
