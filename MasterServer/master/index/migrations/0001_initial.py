# Generated by Django 3.1.4 on 2020-12-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=200)),
                ('schoolAddress', models.CharField(max_length=200)),
                ('schoolType', models.CharField(max_length=200)),
                ('schoolDescription', models.TextField()),
            ],
        ),
    ]
