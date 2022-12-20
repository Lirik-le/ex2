# Generated by Django 4.1.4 on 2022-12-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/product', verbose_name='Картинка')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
        ),
    ]