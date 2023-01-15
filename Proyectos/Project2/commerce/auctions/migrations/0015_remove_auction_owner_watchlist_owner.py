# Generated by Django 4.1 on 2023-01-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_remove_watchlist_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='Owner',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='Owner',
            field=models.CharField(blank=True, default='owner', max_length=50, null=True),
        ),
    ]