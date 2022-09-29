import email
from rest_framework import generics, viewsets, mixins
from . models import User
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


class SpecificUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'memberId'

class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','post','retrieve','put','patch']

    class UserViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.

        """
        queryset = User.objects.all()
        serializer_class = UserSerializer
        http_method_names = ['get','post','retrieve','put','patch']
