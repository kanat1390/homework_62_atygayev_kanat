from django.db import models
from django.urls import reverse

class TaskManager(models.Manager):
    def get_queryset(self):
        query_set =  super().get_queryset()
        return query_set.filter(project__is_deleted=False)

class Task(models.Model):
    summary = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(to='tracker.Project', on_delete=models.CASCADE, related_name='tasks')
    status = models.ForeignKey(to='tracker.Status', on_delete=models.PROTECT)
    types = models.ManyToManyField('tracker.Type', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    task_objects = TaskManager()

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk':self.id})

    def __str__(self):
        return self.summary
