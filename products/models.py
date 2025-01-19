from django.db import models

from config.settings import NULLABLE
from users.models import User


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=150, verbose_name='Название', help_text='Введите название продукта')
    model = models.CharField(max_length=150, verbose_name='Модель', help_text='Введите название модели продукта')
    release_data = models.DateField(
        max_length=150,
        verbose_name='Дата выхода продукта на рынок',
        help_text='Введите дату выхода продукта на рынок'
    )
    price = models.FloatField(default=0, verbose_name='Стоимость товара')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.name} модель {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
