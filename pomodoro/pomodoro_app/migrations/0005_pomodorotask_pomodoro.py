# Generated by Django 3.2 on 2023-05-02 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0004_remove_pomodorotask_pomodoro'),
    ]

    operations = [
        migrations.AddField(
            model_name='pomodorotask',
            name='pomodoro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pomodoro_app.pomodoro'),
        ),
    ]
