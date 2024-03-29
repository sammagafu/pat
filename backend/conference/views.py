from rest_framework import generics
from . models import Conference
from . serializers import ConferenceSerializer


class ConferenceListView(generics.ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceDetailView(generics.RetrieveAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    lookup_field = 'slug'
