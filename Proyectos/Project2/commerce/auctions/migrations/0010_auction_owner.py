# Generated by Django 4.1 on 2023-01-08 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_category_categoriename'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='Owner',
            field=models.ForeignKey(blank=b'I01\n', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
