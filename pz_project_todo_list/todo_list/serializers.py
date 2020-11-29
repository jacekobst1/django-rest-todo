from rest_framework import serializers
from pz_project_todo_list.todo_list.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id', 'title', 'created_at', 'updated_at']
