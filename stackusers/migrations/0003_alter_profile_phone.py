# Generated by Django 3.2.8 on 2021-10-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0002_auto_20211007_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
