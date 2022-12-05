from django.db import models

from client.models import Client


class Send(models.Model):
    time_start = models.DateTimeField()
    text = models.TextField()
    filters_of_send = models.JSONField()
    time_end = models.DateTimeField()

    def __str__(self):
        return f"Время начала рассылки {self.time_start} - {self.time_end}"

    class Meta:
        verbose_name = "Send"
        verbose_name_plural = "Sends"


class Message(models.Model):
    create_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    sends = models.ForeignKey(
        Send,
        on_delete=models.CASCADE,
        related_name="send",
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="client"
    )

    def __str__(self):
        return f"Сообщение для клиента {self.client}"

    class Meta:
        ordering = ("create_data",)
