# Generated by Django 3.0.5 on 2021-08-22 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20210822_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
