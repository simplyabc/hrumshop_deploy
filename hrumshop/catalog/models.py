from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')
    slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категоря'
        verbose_name_plural = 'Категории'
        ordering = ('id',)
        index_together = (('id', 'slug'),)


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование')
    slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    price = models.FloatField(default=0, verbose_name='Цена')
    description = models.CharField(max_length=255, verbose_name='Описание')
    old = models.CharField(max_length=25, default='Для взрослых собак', verbose_name='Возраст')
    ingredients = models.CharField(max_length=255, verbose_name='Ингредиенты')
    breed = models.CharField(max_length=25, default='Для всех пород', verbose_name='Порода')
    weight = models.FloatField(default=0, verbose_name='Вес')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)
        index_together = (('id', 'slug'),)
