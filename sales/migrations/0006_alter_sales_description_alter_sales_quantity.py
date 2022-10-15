# Generated by Django 4.1 on 2022-10-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_sales_valid_alter_sales_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='quantity',
            field=models.FloatField(null=True, verbose_name='Quantity (in kg)'),
        ),
    ]
