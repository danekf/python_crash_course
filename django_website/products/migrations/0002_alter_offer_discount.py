# Generated by Django 4.1.3 on 2022-11-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.FloatField(),
        ),
    ]
