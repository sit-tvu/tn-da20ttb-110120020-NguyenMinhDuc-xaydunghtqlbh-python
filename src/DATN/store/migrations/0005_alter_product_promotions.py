# Generated by Django 5.0.4 on 2024-06-09 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_promotions_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.PositiveIntegerField(),
        ),
    ]
