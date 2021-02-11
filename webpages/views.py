from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tasks_and_tags.models import Tag, Task
from .forms import ContactForm
from .filters import TaskFilter

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            # send email
            return redirect('tasks')
    else:
        form = ContactForm()
    return render(request, 'webpages/contact.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    tasks = user.task_set.all()
    tags = user.tag_set.all()
    #myFilter = TaskFilter()
    myFilter = TaskFilter(request.GET,queryset=tasks)
    tasks=myFilter.qs
    totaltasks=tasks.count()
    completedtasks=tasks.filter(status = 'CO').count()
    totaltags = tags.count()
    return render(request, 'webpages/dashboard.html', {'tasks': tasks,
                                                       'tags': tags,
                                                       'myFilter':myFilter,
                                                       'totaltasks':totaltasks,
                                                       'completedtasks':completedtasks,
                                                       'totaltags':totaltags,
                                                       })

@login_required(login_url='login')
def side_navbar(request):
    return render(request, 'webpages/side_navbar.html')

