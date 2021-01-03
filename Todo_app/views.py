from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Tasks
from .forms import NameForm



def index(request, **kw):
        
        global last_kw
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                content = form.cleaned_data["content"]
                task = form.cleaned_data["task"]
                new_task = Tasks(task_category=content, task_text = task, pub_date=timezone.now())
                new_task.save()
        if kw:
            last_kw = kw["filter"]
            latest_task_list = Tasks.objects.filter(task_category=kw['filter'])
        else:
            last_kw = "dashboard"
            latest_task_list = Tasks.objects.all()
        form = NameForm()
        staff_for_frontend = {
            'latest_task_list': latest_task_list,
            'form': form,
            }
        return render(request, 'Todo_app/index.html', staff_for_frontend)



def delete_task(request, id):
    Tasks.objects.filter(id=id).delete()
    
    if last_kw == "dashboard":
        return redirect('index')
    else:
        return redirect('index', filter=last_kw)
    


def change_line(request, id):
    """ changing style of checked or unchecked task """


    change = Tasks.objects.get(id=id)
    if change.s_type == "undone" :
        change.s_type = "done"
        change.save()
    else:
        change.s_type = "undone"
        change.save()

    if last_kw == "dashboard":
        return redirect('index')
    else:
        return redirect('index', filter=last_kw)

class TaskCreatView(CreateView):
    model = Tasks
    fields = ('task_category', 'task_text')

