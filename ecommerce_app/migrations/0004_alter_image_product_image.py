# Generated by Django 4.1.4 on 2023-02-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ecommerce_app",
            "0003_attribute_category_product_specification_product_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="image_product",
            name="image",
            field=models.FilePathField(path="/image"),
        ),
    ]
