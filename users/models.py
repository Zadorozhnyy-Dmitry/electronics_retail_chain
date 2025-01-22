from django.db import models
from django.contrib.auth.models import AbstractUser

from config.settings import NULLABLE


class User(AbstractUser):
    """Класс для описания пользователя"""

    username = models.CharField(
        unique=True,
        max_length=150,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя",
    )
    email = models.EmailField(
        verbose_name="Почта", help_text="Укажите почту", **NULLABLE
    )
    is_active = models.BooleanField(
        default=False,
        help_text="Активируйте учетную запись пользователя для работы с приложением",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
