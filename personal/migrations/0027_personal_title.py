# Generated by Django 3.0.5 on 2021-09-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0026_remove_personal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
