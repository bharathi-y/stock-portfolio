# Generated by Django 2.2 on 2020-08-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_auto_20200813_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allstock',
            name='Type',
            field=models.CharField(blank=True, choices=[('Div', 'Div'), ('Sell', 'Sell'), ('Buy', 'Buy'), ('Split', 'Split'), ('CapReduct', 'CapReduct')], max_length=10, null=True),
        ),
    ]