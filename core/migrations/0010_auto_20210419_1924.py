# Generated by Django 2.2.14 on 2021-04-19 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_order_refund_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
