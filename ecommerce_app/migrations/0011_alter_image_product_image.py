# Generated by Django 4.1.4 on 2023-02-26 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0010_remove_attribute_value_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image_product",
            name="image",
            field=models.ImageField(upload_to="image"),
        ),
    ]