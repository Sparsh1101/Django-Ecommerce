# Generated by Django 2.2.14 on 2021-04-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210413_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(default='defualt'),
            preserve_default=False,
        ),
    ]
