# Generated by Django 3.2 on 2023-05-02 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0003_alter_pomodorotask_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomodorotask',
            name='pomodoro',
        ),
    ]
