from django.db.models import Q
from django.shortcuts import get_list_or_404, get_object_or_404

from client.models import Client
from client.serializers import ClientProfileSerializer

from .abstract_service import ServiceAbctract


class ClientService(ServiceAbctract):
    @staticmethod
    def _get_client_object(client_id):
        client = get_object_or_404(Client, client_id=client_id)
        return client

    @classmethod
    def validate_data_method_post(cls, serializer):
        serializer.is_valid(raise_exception=True)
        return serializer.data

    @classmethod
    def validate_data_method_put(cls, client_id, data):
        client = cls._get_client_object(client_id=client_id)
        serializer = ClientProfileSerializer(client, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    @classmethod
    def method_get_of_list_is_validate(cls, query_params):
        list_clients = get_list_or_404(Client, **query_params)
        serializer = ClientProfileSerializer(data=list_clients, many=True)
        return serializer.data

    @classmethod
    def method_get_client_info(cls, client_id, data):
        client = cls._get_client_object(client_id=client_id)
        serializer = ClientProfileSerializer(client, data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    @classmethod
    def get_queryset_of_messages_by_client_id(cls, client_id):
        client = cls._get_client_object(client_id=client_id)
        return client.client.all()

    @classmethod
    def searching_by_filters(cls, tag, code_of_mobile_operator):
        queryset = Client.objects.filter(
            Q(tag=tag) | Q(code_of_mobile_operator=code_of_mobile_operator)
        )
        return queryset

    @classmethod
    def delete(cls, client_id):
        client = cls._get_client_object(client_id=client_id)
        client.delete()

    @classmethod
    def create(cls, validate_data, serializer):
        return serializer.create(validate_data)

    @classmethod
    def update(cls, client):
        return client.save()
