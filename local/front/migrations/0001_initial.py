# Generated by Django 3.0 on 2019-12-05 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64)),
                ('conform_password', models.CharField(max_length=64)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
