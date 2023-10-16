from django.db import models
from django.utils import timezone

class Task(models.Model):

    STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title