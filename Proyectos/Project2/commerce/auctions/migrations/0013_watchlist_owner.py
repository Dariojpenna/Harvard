# Generated by Django 4.1 on 2023-01-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_watchlist_owner_alter_auction_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='Owner',
            field=models.CharField(blank=True, default='owner', max_length=50, null=True),
        ),
    ]