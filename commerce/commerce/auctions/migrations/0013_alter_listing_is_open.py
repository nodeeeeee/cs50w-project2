# Generated by Django 5.1.3 on 2024-11-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_listing_is_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
