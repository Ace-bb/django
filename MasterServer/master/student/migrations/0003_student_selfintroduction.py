# Generated by Django 3.1.4 on 2020-12-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_hadsendmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='selfIntroduction',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
