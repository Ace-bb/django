# Generated by Django 3.1.4 on 2020-12-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordId', models.CharField(max_length=100)),
                ('sendTime', models.DateTimeField()),
                ('sendId', models.CharField(max_length=100)),
                ('receiveId', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatRoomId', models.CharField(max_length=100)),
                ('studentId', models.CharField(max_length=100)),
                ('teacherId', models.CharField(max_length=100)),
                ('chatRoomTime', models.DateTimeField()),
            ],
        ),
    ]
