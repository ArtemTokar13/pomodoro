from django.forms import ModelForm
from .models import Pomodoro, PomodoroTask


class PomodoroTaskForm(ModelForm):
    class Meta:
        model = PomodoroTask
        fields = ['title', 'is_done']
        
class PomodoroForm(ModelForm):
    class Meta:
        model = Pomodoro
        fields = []