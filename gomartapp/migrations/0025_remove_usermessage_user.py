# Generated by Django 4.2.6 on 2023-10-22 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0024_usermessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='user',
        ),
    ]
