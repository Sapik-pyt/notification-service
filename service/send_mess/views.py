from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from send_mess.services.send_message_services import SendMessageServices


class GetOrPostMethodSendView(APIView):

    def get(self, request):
        list_send_message = SendMessageServices.method_get_of_list_is_validate(
            request.data
        )
        return Response(data=list_send_message, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SendMessageServices.validate_data_method_post(
            request.data
        )
        data = SendMessageServices.create(serializer)
        return Response(data=data, status=status.HTTP_201_CREATED)


class UpdateOrDeleteSendView(APIView):

    def get(self, request, send_id):
        query_params = request.query_params
        data = SendMessageServices.method_get_client_info(
            send_id=send_id,
            query_params=query_params
        )
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, send_id):
        send_object = SendMessageServices.validate_data_method_put(
            send_id=send_id,
            data=request.data
        )
        send_object_update = SendMessageServices.update(send_object)
        return Response(data=send_object_update, status=status.HTTP_200_OK)

    def delete(self, request, send_id):
        SendMessageServices.delete(send_id=send_id)
        return Response(
            {"message": "Рассылка удалена"},
            status=status.HTTP_200_OK
        )
