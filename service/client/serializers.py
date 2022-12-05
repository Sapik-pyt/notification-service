from rest_framework.serializers import ModelSerializer

from client.models import Client


class ClientProfileSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"
