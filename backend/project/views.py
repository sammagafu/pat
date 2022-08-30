from rest_framework import generics
from . models import Project
from .serializer import ProjectSerializer



class ProjectsList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer