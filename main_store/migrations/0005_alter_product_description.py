# Generated by Django 3.2.7 on 2021-10-09 01:15

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_store', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, default='', max_length=800, null=True),
        ),
    ]
