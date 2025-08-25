from django.db import models

class Task(models.Model):
    STATUS = (('todo','To Do'), ('inprogress','In Progress'), ('done','Done'))
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
