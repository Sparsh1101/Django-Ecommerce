# Generated by Django 2.2.14 on 2021-04-19 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210419_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='one_click_purchasing',
        ),
    ]
