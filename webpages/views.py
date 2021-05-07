from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tasks_and_tags.models import Tag, Task

from .filters import TaskFilter
from .models import ContactModel


def contact(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        obj = ContactModel(name=name, email=email, subject=subject, message=message)
        obj.save()
        return redirect('dashboard')
    return render(request, 'webpages/contact.html')


@login_required(login_url='login')
def dashboard(request):
    #tasks = task.objects.all()
    #tags = tag.objects.all()
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

