# Generated by Django 3.0.5 on 2021-08-22 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20210821_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='fromdate',
            field=models.CharField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=datetime.datetime.now, max_length=20),
        ),
    ]
