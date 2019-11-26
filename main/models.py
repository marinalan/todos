from django.db import models

# Create your models here.
class Todo(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'
    STATE_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done')
    ]
    description = models.TextField()
    due_date = models.DateField()
    state = models.CharField(
        max_length=11,
        choices=STATE_CHOICES,
        default=TODO
    )

    def _title(self):
        nl = self.description.find("\n")
        lb = min(120, nl) if nl > -1 else 120
        return self.description[:lb]

    title = property(_title)

    def __str__(self):
        return self.title
