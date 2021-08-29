# Generated by Django 3.0 on 2020-10-16 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderAndDelivery', '0012_auto_20201016_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Online Transfered/ Online Payment'), ('3', 'Cash In Hand')], default='1', max_length=100),
        ),
    ]
