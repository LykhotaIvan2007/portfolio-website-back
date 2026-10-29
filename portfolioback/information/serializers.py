from rest_framework import serializers
from .models import Projects, Documents

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"
