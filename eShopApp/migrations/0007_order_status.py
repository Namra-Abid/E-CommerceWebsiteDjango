# Generated by Django 4.1.7 on 2023-04-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eShopApp', '0006_alter_order_address_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]