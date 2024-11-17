# Generated by Django 5.1.3 on 2024-11-17 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_category_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
            preserve_default=False,
        ),
    ]
