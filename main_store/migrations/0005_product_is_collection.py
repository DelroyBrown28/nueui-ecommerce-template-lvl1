# Generated by Django 3.2.7 on 2021-11-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0004_alter_product_link_to_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
    ]
