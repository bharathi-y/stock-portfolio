# Generated by Django 2.2 on 2020-08-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0013_auto_20200815_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allstock',
            name='fee',
            field=models.FloatField(help_text='Fee Payed '),
        ),
        migrations.AlterField(
            model_name='allstock',
            name='transaction_price_per_unit',
            field=models.FloatField(help_text='price per unit'),
        ),
    ]