# Generated by Django 4.1.4 on 2023-03-02 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce_app", "0016_rename_product_tag_product_product"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tags",
            old_name="tag",
            new_name="name",
        ),
    ]
