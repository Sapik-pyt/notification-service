from django.urls import path

from send_mess.views import GetOrPostMethodSendView, UpdateOrDeleteSendView

urlpatterns = [
    path(
        'send_message/',
        GetOrPostMethodSendView.as_view(),
        name='send_message_get_or_create'
    ),
    path(
        'send_message/<send_id>',
        UpdateOrDeleteSendView.as_view(),
        name='send_mes_del_or_update'
    )
]
