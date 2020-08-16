# Generated by Django 2.2 on 2020-08-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0021_auto_20200815_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_stock',
            name='fee',
            field=models.IntegerField(blank=True, help_text='Fee Payed ', null=True),
        ),
        migrations.AlterField(
            model_name='all_stock',
            name='transaction_price_per_unit',
            field=models.IntegerField(blank=True, help_text='price per unit', null=True),
        ),
    ]