# Generated by Django 3.0.5 on 2021-08-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0019_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
