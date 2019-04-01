from django.db import models

# Create your models here.
class TodoItems(models.Model) :
    todo_items = models.TextField()

    def __str__(self):
        return self.todo_items[:10]
