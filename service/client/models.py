from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Client(AbstractUser):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_validate = RegexValidator(
        regex=r'7\d{10}',
        message="Формат номера должен быть в виде 7XXXXXXXXXX (X - от 0 до 9)"
    )
    phone = models.CharField(
        "Номер телефона",
        validators=[phone_validate],
        max_length=11,
        unique=True
    )
    code_operator = models.CharField(
        "Код оператора",
        max_length=3,
        editable=False
    )
    tag = models.CharField("Тег", max_length=10)
    time_zone = models.CharField(
        "Часовой пояс",
        max_length=32,
        choices=TIMEZONES,
        default="UTC"
    )

    def __str__(self):
        return f"Клиент {self.id} - номер телефона {self.phone}"

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        self.code_operator = str(self.phone)[1:4]
        super().save(force_insert, force_update, using, update_fields)
