# Generated by Django 4.1.5 on 2023-01-29 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('binance_helper', '0006_remove_binance_profile_total_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='binance_profile',
            name='total_wallet',
            field=models.FloatField(default=0),
        ),
    ]
