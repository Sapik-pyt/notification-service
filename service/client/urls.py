from django.urls import path

from client.views import CreateCLientInDirectoryView, DeleteOrUpdateClentView

urlpatterns = [
    path(
        'client/',
        CreateCLientInDirectoryView.as_view(),
        name='client-create-get'
    ),
    path(
        'client/<client_id>/',
        DeleteOrUpdateClentView.as_view(),
        name='client-delete-update'
    )
]
