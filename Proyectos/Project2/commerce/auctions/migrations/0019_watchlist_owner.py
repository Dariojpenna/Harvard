# Generated by Django 4.1 on 2023-01-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auction_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='Owner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
