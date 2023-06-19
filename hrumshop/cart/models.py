from django.db import models
from django.core.validators import RegexValidator
from catalog.models import Product


class Order(models.Model):
    name = models.CharField(max_length=24, verbose_name='Имя')
    phone = models.CharField(max_length=16, blank=True, null=True, verbose_name='Телефон')
    address = models.CharField(max_length=64, blank=True, null=True, verbose_name='Адрес доставки')
    comments = models.CharField(max_length=500, blank=True, null=True, verbose_name='Комментарий')
    total_price = models.FloatField(default=0, verbose_name='Сумма заказа')
    condition = models.BooleanField(default=False, verbose_name='Выполнение')
    created = models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Создан')

    def __str__(self):
        return f'Заказ № {str(self.id)}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('id',)


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='ID Товара')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Заказанные товары'
        ordering = ('id',)
