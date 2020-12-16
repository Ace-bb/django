# Generated by Django 3.1.4 on 2020-12-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.CharField(max_length=200)),
                ('courseName', models.CharField(max_length=200)),
                ('teacherName', models.CharField(max_length=200)),
                ('classTime', models.DateTimeField()),
                ('courseLable', models.CharField(max_length=200)),
                ('studentNum', models.IntegerField()),
            ],
        ),
    ]