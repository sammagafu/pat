from rest_framework import generics
from .serializer import UpdateSerializer
from .models import Updates
# Create your views here.

class UpdateList(generics.ListCreateAPIView):
    queryset = Updates.objects.all()
    serializer_class = UpdateSerializer

class UpdateDetailView(generics.RetrieveAPIView):
    queryset = Updates.objects.all()
    serializer_class = UpdateSerializer
    lookup_field = 'slug'