# Generated by Django 3.0 on 2019-12-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_model',
            name='conform_password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration_model',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
