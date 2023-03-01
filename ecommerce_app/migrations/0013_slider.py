# Generated by Django 4.1.1 on 2023-03-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0012_alter_image_product_image_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=100)),
                ('action_name', models.CharField(max_length=50)),
                ('link', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/slider/%Y/%m/%d/')),
            ],
        ),
    ]
