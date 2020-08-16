# Generated by Django 2.2 on 2020-08-15 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_auto_20200814_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allstock',
            name='Currency',
        ),
        migrations.RemoveField(
            model_name='allstock',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='allstock',
            name='Stock',
        ),
        migrations.RemoveField(
            model_name='allstock',
            name='TransactionPrice',
        ),
        migrations.RemoveField(
            model_name='allstock',
            name='TransactionUnit',
        ),
        migrations.RemoveField(
            model_name='allstock',
            name='Type',
        ),
        migrations.AddField(
            model_name='allstock',
            name='currency',
            field=models.CharField(choices=[('USD', 'United States Dollar'), ('HKD', 'Hong Kong dollar')], default=django.utils.timezone.now, help_text='choice the currenct ', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allstock',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, help_text='Date of transaction', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allstock',
            name='fee',
            field=models.FloatField(default=django.utils.timezone.now, help_text='Fee Payed ', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allstock',
            name='stock',
            field=models.CharField(default=django.utils.timezone.now, help_text='please select the stock', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allstock',
            name='transaction_price_per_unit',
            field=models.FloatField(default=django.utils.timezone.now, help_text='price per unit', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allstock',
            name='transaction_unit',
            field=models.IntegerField(default=django.utils.timezone.now, help_text='number of stocks transacted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allstock',
            name='type',
            field=models.CharField(blank=True, choices=[('Sell', 'Sell'), ('Buy', 'Buy')], help_text='Bought or sell', max_length=8, null=True),
        ),
    ]