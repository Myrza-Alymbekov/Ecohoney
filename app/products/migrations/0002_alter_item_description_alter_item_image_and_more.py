# Generated by Django 4.1.7 on 2023-02-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Остатки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='volume',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Объём тары'),
        ),
    ]