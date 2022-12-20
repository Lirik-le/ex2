from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=False)
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='product', verbose_name='Картинка', blank=False)
    price = models.IntegerField(default=0, verbose_name='Цена', blank=False)
