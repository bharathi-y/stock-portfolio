# Generated by Django 2.2 on 2020-08-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0016_auto_20200815_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allstock',
            name='TransactionPrice',
            field=models.IntegerField(max_length=100),
        ),
    ]
