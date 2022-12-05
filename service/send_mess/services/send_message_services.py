from django.db.models import Q
from django.shortcuts import get_object_or_404

from send_mess.models import Send
from send_mess.serializers import SendSerializers

from .abstract_service import ServiceAbctract


class SendMessageServices(ServiceAbctract):

    @staticmethod
    def _get_object_of_sends(send_id):
        sends_message = get_object_or_404(Send, send_id=send_id)
        return sends_message

    @classmethod
    def validate_data_method_post(cls, data):
        serializer = SendSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    @classmethod
    def method_get_of_list_is_validate(cls, data):
        serializaer = SendSerializers(data=data, many=True)
        serializaer.is_valid(raise_exception=True)
        return serializaer.data

    @classmethod
    def searching_by_filters(cls, tag, code_operator):
        queryset = Send.objects.filter(
            Q(filters_of_send__tag=tag) | Q(
                filters_of_send__code_operator=code_operator)
        )
        return queryset

    @classmethod
    def get_queryset_of_messages_by_mailing_id(cls, send_id):
        send = cls._get_object_of_sends(send_id=send_id)
        return send.sends.all()

    @classmethod
    def method_get_client_info(cls, send_id, query_params):
        send_object = cls._get_object_of_sends(send_id=send_id)
        serializer = SendSerializers(send_object, **query_params)
        return serializer.data

    @classmethod
    def validate_data_method_put(cls, send_id, data):
        send_object = cls._get_object_of_sends(send_id=send_id)
        serializer = SendSerializers(send_object, data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    @classmethod
    def post(cls, serializer):
        return serializer.save()

    @classmethod
    def delete(cls, send_id):
        send_object = cls._get_object_of_sends(send_id=send_id)
        send_object.delete()

    @classmethod
    def update(cls, send):
        return send.save()
