# Generated by Django 4.1.4 on 2023-03-08 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0026_alter_featuredproducut_experation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="featuredproducut",
            name="experation_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 3, 10, 11, 38, 51, 392520, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
