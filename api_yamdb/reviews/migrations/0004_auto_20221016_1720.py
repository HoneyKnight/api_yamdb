# Generated by Django 2.2.16 on 2022-10-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221011_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]