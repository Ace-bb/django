# Generated by Django 3.1.4 on 2020-12-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_auto_20201216_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatHistroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=100)),
                ('studentName', models.CharField(max_length=100)),
                ('taecherName', models.CharField(max_length=100)),
                ('teacherIcon', models.CharField(max_length=500)),
                ('lastMessage', models.CharField(max_length=200)),
            ],
        ),
    ]