# Generated by Django 3.2.7 on 2021-10-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
    ]
