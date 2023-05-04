from django.db import models
from datetime import datetime


class Pomodoro(models.Model):
    start_on = models.DateTimeField(auto_now=False, auto_now_add=False,
                                    default=datetime.now(), blank=True)
    end_on = models.DateTimeField(null=True, blank=True)

class PomodoroTask(models.Model):
    title = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)
    pomodoro = models.ForeignKey(Pomodoro, blank=True, null=True,
                                 on_delete=models.CASCADE)
