# Generated by Django 3.2 on 2023-05-02 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pomodorotask',
            old_name='task',
            new_name='title',
        ),
    ]