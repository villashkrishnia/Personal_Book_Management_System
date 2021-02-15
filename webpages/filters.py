import django_filters
from tasks_and_tags.models import *

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['content']
