# Generated by Django 3.2 on 2023-05-03 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0008_auto_20230503_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomodoro',
            name='pomodoro_duration',
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='end_on',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 5, 3, 22, 6, 32, 500642)),
        ),
        migrations.AddField(
            model_name='pomodoro',
            name='start_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 3, 22, 6, 32, 500642)),
        ),
    ]