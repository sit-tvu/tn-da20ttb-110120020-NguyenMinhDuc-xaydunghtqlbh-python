# Generated by Django 5.0.4 on 2024-06-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_promotions'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]