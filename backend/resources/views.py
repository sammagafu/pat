from rest_framework import generics
from . models import Resource
from .serializer import ResourceSerializer



class ResourcesList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer