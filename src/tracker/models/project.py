from django.db import models
from django.contrib.auth.models import User

class ProjectManager(models.Manager):
    def get_queryset(self):
        query_set =  super().get_queryset()
        return query_set.filter(is_deleted=False)

class Project(models.Model):
    started_date = models.DateField()
    finished_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    objects = models.Manager()
    project_objects = ProjectManager()
    participants = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
    
    
        
