# Generated by Django 3.2 on 2023-05-02 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pomodoro_app', '0006_alter_pomodorotask_pomodoro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodorotask',
            name='pomodoro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pomodoro_app.pomodoro'),
        ),
    ]