import datetime
import os

import pytz
import requests
from celery.utils.log import get_task_logger
from django.shortcuts import get_object_or_404

from client.models import Client
from send_mess.models import Message, Send
from service.celery import app

logger = get_task_logger(__name__)


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, sends_id, client_id):
    send = get_object_or_404(Send, id=sends_id)
    client = get_object_or_404(Client, id=client_id)
    token = os.getenv('TOKEN_SERVICE')
    url_adress = os.getenv('URL_SERVICE')

    timezone = pytz.timezone(client.time_zone)
    time_now = datetime.datetime.now(timezone).astimezone(pytz.UTC)
    time_start = send.time_start.replace(tzinfo=timezone).astimezone(pytz.UTC)
    time_end = send.time_end.replace(tzinfo=timezone).astimezone(pytz.UTC)

    if time_start <= time_now <= time_end:
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        try:
            requests.post(
                url=url_adress + str(data['id']),
                headers=headers,
                json=data
            )
        except Exception as error:
            logger.error(f"Сообщение id для {data['id']} is error")
            raise f"Error - {error}"
        else:
            logger.info(f"Сообщение id: {data['id']}, статус: 'Отправлено'")
            Message.objects.filter(id=data['id']).update(status=True)
    else:
        time = (time_start - time_now).seconds
        logger.info(
            f"Перезапуск задачи через {time + 1} секунд"
        )
