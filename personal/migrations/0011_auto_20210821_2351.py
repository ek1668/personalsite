# Generated by Django 3.0.5 on 2021-08-22 03:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_auto_20210821_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='fromdate',
            field=models.DateField(blank=True, default=datetime.datetime),
        ),
    ]
