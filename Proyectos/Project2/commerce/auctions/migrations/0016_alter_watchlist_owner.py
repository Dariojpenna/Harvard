# Generated by Django 4.1 on 2023-01-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_remove_auction_owner_watchlist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='Owner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
