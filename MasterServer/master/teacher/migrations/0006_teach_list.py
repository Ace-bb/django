# Generated by Django 3.1.4 on 2020-12-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_delete_teach_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teach_list',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacherId', models.CharField(max_length=200)),
                ('teacherName', models.CharField(max_length=100)),
                ('you_can_learn', models.CharField(max_length=100)),
            ],
        ),
    ]
