# Generated by Django 3.1.4 on 2020-12-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HadSendMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_name', models.CharField(max_length=100)),
                ('school_grade', models.CharField(max_length=100)),
                ('send_message', models.TextField(max_length=1000)),
            ],
        ),
    ]
