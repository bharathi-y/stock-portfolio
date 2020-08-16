# Generated by Django 2.2 on 2020-08-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0018_remove_allstock_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allstock',
            old_name='Stock',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='allstock',
            name='Currency',
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
            field=models.CharField(blank=True, choices=[('USD', 'United States Dollar'), ('HKD', 'Hong Kong dollar')], help_text='choice the currenct ', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='allstock',
            name='date',
            field=models.CharField(blank=True, help_text='Date of transaction', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='allstock',
            name='fee',
            field=models.FloatField(blank=True, help_text='Fee Payed ', null=True),
        ),
        migrations.AddField(
            model_name='allstock',
            name='transaction_price_per_unit',
            field=models.FloatField(blank=True, help_text='price per unit', null=True),
        ),
        migrations.AddField(
            model_name='allstock',
            name='transaction_unit',
            field=models.IntegerField(blank=True, help_text='number of stocks transacted', null=True),
        ),
        migrations.AddField(
            model_name='allstock',
            name='type',
            field=models.CharField(blank=True, choices=[('Sell', 'Sell'), ('Buy', 'Buy')], help_text='Bought or sell', max_length=8, null=True),
        ),
    ]
