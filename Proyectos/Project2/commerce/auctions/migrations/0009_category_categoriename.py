# Generated by Django 4.1 on 2022-10-15 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auction_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='CategorieName',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]