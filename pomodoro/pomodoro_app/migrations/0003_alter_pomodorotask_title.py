# Generated by Django 3.2 on 2023-05-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0002_rename_task_pomodorotask_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodorotask',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]