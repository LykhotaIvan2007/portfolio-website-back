from django.shortcuts import render
from rest_framework import generics

from .models import Projects
from .serializers import *

# Create your views here.


class RetrieveProjects(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class RetrieveDocs(generics.ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocsSerializer



