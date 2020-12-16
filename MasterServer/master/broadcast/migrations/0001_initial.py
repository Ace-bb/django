# Generated by Django 3.1.4 on 2020-12-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcastRoomId', models.CharField(max_length=100)),
                ('roomName', models.CharField(max_length=200)),
                ('teacherName', models.CharField(max_length=100)),
                ('teacherId', models.CharField(max_length=100)),
                ('liveTime', models.DateTimeField()),
                ('broadcastTitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='roomEvaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broadcastRoomId', models.CharField(max_length=100)),
                ('evaluateTime', models.DateTimeField()),
                ('evaluateMessage', models.TextField()),
                ('evaluateAccount', models.CharField(max_length=100)),
            ],
        ),
    ]
