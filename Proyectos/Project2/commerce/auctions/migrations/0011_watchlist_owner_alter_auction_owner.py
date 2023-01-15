# Generated by Django 4.1 on 2023-01-08 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auction_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='Owner',
            field=models.CharField(default='owner', max_length=50),
        ),
        migrations.AlterField(
            model_name='auction',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]