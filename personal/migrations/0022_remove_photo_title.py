# Generated by Django 3.0.5 on 2021-08-22 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0021_photo_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
    ]
