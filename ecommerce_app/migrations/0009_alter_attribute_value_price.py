# Generated by Django 4.1.4 on 2023-02-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0008_alter_image_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attribute_value",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
