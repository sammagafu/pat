from rest_framework import serializers
from .models import Resource,ResourceCategory

class ResourceCategory(serializers.ModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = ['title']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id','title', 'file','description','published', 'category', 'created','get_file']
