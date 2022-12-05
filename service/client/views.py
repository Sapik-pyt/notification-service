from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from client.serializers import ClientProfileSerializer
from send_mess.services.client_services import ClientService


class CreateCLientInDirectoryView(APIView):

    def get(self, request):
        query = request.query_params
        data_validate = ClientService.method_get_of_list_is_validate(
            query_params=query
        )
        return Response(data=data_validate, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClientProfileSerializer(data=request.data)
        validate_data = ClientService.validate_data_method_post(
            serializer=serializer
        )
        ClientService.create(
            validate_data=validate_data,
            serializer=serializer
        )
        return Response(data=validate_data, status=status.HTTP_201_CREATED)


class DeleteOrUpdateClentView(APIView):

    def get(self, request, client_id):
        client = ClientService.method_get_client_info(
            client_id=client_id,
            data=request.data
        )
        return Response(data=client, status=status.HTTP_200_OK)

    def put(self, requset, client_id):
        client = ClientService.validate_data_method_put(
            data=requset.data,
            client_id=client_id
        )
        client_info_update = ClientService.update(client)
        return Response(
            data=client_info_update,
            status=status.HTTP_200_OK
        )

    def delete(self, request, client_id):
        ClientService.delete(client_id=client_id)
        return Response(
            {"message": "Клиент был удален"},
            status=status.HTTP_200_OK
        )
