# Generated by Django 4.1.7 on 2023-06-02 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Создан')),
                ('name', models.CharField(max_length=24, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=64, null=True, verbose_name='Адрес доставки')),
                ('comments', models.CharField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('total_price', models.FloatField(default=0, verbose_name='Сумма заказа')),
                ('condition', models.BooleanField(default=False, verbose_name='Выполнение')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Номер заказа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.product', verbose_name='ID Товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Заказанные товары',
                'ordering': ('id',),
            },
        ),
    ]
