# Generated by Django 4.1.4 on 2023-02-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0008_alter_image_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image_product",
            name="image",
            field=models.FilePathField(
                blank=True,
                path="ecommerce_app/media/image/pro_<django.db.models.query_utils.DeferredAttribute object at 0x000001724C33BD60>",
            ),
        ),
    ]
