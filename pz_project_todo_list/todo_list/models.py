from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']


class TodoItem(models.Model):
    list_id = models.ForeignKey(TodoList, related_name='items', on_delete=models.CASCADE, db_column='list_id')
    name = models.CharField(max_length=100)
    done_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
