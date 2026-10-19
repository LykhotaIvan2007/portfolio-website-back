from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Test
        fields = "__all__"  # ("title", "content", "cat")

class TestSerializerForOneField(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Test
        fields = ("title", "user") # ("title", "content", "cat")
