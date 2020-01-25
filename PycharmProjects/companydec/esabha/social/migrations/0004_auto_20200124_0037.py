# Generated by Django 3.0.2 on 2020-01-23 19:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20191218_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='age',
            field=models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)]),
        ),
    ]
