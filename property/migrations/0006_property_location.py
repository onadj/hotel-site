# Generated by Django 3.1.4 on 2020-12-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
