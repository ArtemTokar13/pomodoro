from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PomodoroTaskForm, PomodoroForm
from django.forms import HiddenInput
from .models import PomodoroTask, Pomodoro
from datetime import datetime

def index(request):
    is_running = False
    pomodoro_tasks = PomodoroTask.objects.all()
    try:
        running_pomodoro = Pomodoro.objects.get(end_on=None)
        is_running = True
    except:
        running_pomodoro = None
    
    if request.method == 'GET':
        pomodoro_task_form = PomodoroTaskForm()
        pomodoro_form = PomodoroForm()
        pomodoro_task_form.fields['is_done'].widget = HiddenInput()
        return_vars = dict(pomodoro_task_form=pomodoro_task_form,
                           pomodoro_form=pomodoro_form,
                           pomodoro_tasks=pomodoro_tasks,
                           is_running=is_running)
        return render(request, 'pomodoro/index.html', return_vars)
    else:
        form_task = PomodoroTaskForm(request.POST)
        form_pomodoro = PomodoroForm(request.POST)
        if form_task.is_valid():
            new_task = form_task.save(commit=False)
            new_task.save()
        elif form_pomodoro.is_valid():
            new_pomodoro = form_pomodoro.save(commit=False)
            if 'pomodoro' in request.POST and running_pomodoro is None:
                new_pomodoro.start_on = datetime.now()
                new_pomodoro.save()
            elif 'end-submit' in request.POST and running_pomodoro is not None:
                running_pomodoro.end_on = datetime.now()
                running_pomodoro.save()
        return redirect('index')