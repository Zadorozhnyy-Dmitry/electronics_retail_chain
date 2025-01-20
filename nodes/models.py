from django.db import models

from config.settings import NULLABLE
from products.models import Product
from django.core.exceptions import ValidationError

from users.models import User


class ElectronicsRetailNode(models.Model):
    """Модель элемента звена сети"""

    NODE_LEVEL_CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]
    NODE_TIPE_CHOICES = {
        ('f', 'завод'),
        ('n_w', 'розничная сеть'),
        ('IE', 'ИП'),
    }

    name = models.CharField(max_length=150, verbose_name='Название', help_text='Введите название звена сети')
    email = models.EmailField(unique=True, verbose_name='Электронный адрес', help_text='Введите электронный адрес')
    country = models.CharField(max_length=20, verbose_name='Страна', help_text='Введите название страны')
    city = models.CharField(max_length=20, verbose_name='Город', help_text='Введите название города')
    street = models.CharField(max_length=30, verbose_name='Улица', help_text='Введите название улицы')
    home_number = models.CharField(max_length=10, verbose_name='Номер дома', help_text='Введите название номер дома')

    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        **NULLABLE
    )
    debt = models.FloatField(verbose_name='Задолженность перед поставщиком, руб', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    node_level = models.IntegerField(
        choices=NODE_LEVEL_CHOICES,
        default=0,
        verbose_name='Уровень иерархии'
    )
    node_type = models.CharField(
        max_length=20,
        choices=NODE_TIPE_CHOICES,
        default='f',
        verbose_name='Тип звена цепи'
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def clean(self):
        # Проверка поставщика
        if self.supplier and self.supplier.node_level == 2:
            raise ValidationError("Поставщик не может быть с уровнем 2")
        # Проверка уровня иерархии
        if self.supplier and (self.node_level - self.supplier.node_level) != 1:
            raise ValidationError("Собственный уровень иерархии должен быть больше уровня поставщика на единицу")
        if self.supplier is None and self.node_level != 0:
            raise ValidationError("Укажите поставщика или уровень иерархии 0")
        # Проверка типа узла сети
        if self.node_level == 0 and self.node_type != 'f':
            raise ValidationError("Для уровня иерархии 0 укажите 'Завод'")

    def __str__(self):
        return f'{self.name} - уровень {self.node_level}, {self.node_type}'

    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'
