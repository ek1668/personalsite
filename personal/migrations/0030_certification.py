# Generated by Django 3.0.5 on 2021-09-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0029_education_graduation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuer', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('dateissued', models.CharField(max_length=50)),
            ],
        ),
    ]
