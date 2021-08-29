# Generated by Django 3.0 on 2020-10-11 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('OrderAndDelivery', '0002_orderitem_item'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Vendor', '0001_initial'),
        ('CartSystem', '0003_auto_20201011_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(related_name='order_orderItem', to='OrderAndDelivery.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Vendor.Vendor'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CartSystem.Location'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='OrderAndDelivery.Order'),
        ),
    ]