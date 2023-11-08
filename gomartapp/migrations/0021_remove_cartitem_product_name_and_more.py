# Generated by Django 4.2.6 on 2023-10-21 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gomartapp', '0020_remove_cartitem_product_remove_cartitem_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='username',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to='gomartapp.product'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
