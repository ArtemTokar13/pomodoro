# Generated by Django 3.2 on 2023-05-04 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0010_auto_20230503_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodoro',
            name='end_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 4, 23, 5, 13, 12509)),
        ),
        migrations.AlterField(
            model_name='pomodoro',
            name='start_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 4, 23, 5, 13, 12509)),
        ),
    ]