# Generated by Django 4.1.4 on 2023-03-08 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0025_remove_featuredproducut_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="featuredproducut",
            name="experation_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 3, 10, 11, 35, 31, 287702, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
