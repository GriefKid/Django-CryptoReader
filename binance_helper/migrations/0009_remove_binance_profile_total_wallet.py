# Generated by Django 4.1.5 on 2023-01-29 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('binance_helper', '0008_alter_binance_profile_total_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binance_profile',
            name='total_wallet',
        ),
    ]