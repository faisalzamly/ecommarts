# Generated by Django 4.1.4 on 2023-02-26 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0006_alter_image_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image_product",
            name="image",
            field=models.ImageField(upload_to="image"),
        ),
    ]
