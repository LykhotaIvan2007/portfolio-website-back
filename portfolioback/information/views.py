from django.shortcuts import render
from rest_framework import generics

from .models import Test
from .serializers import *

# Create your views here.


class TestRetrieveInfo(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer



