# Generated by Django 4.1 on 2023-01-08 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_watchlist_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='Owner',
        ),
    ]