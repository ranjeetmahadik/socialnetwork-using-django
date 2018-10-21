from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy
User = get_user_model()

class UserDataSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
        "username",
        "first_name",
        "last_name",
        "url"
        ]

    def get_url(self,obj):
        return reverse_lazy("profiles:detail",kwargs={"username":obj.username})
