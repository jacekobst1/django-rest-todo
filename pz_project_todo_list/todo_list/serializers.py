from rest_framework import serializers
from pz_project_todo_list.todo_list.models import TodoItem, TodoList


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'list_id', 'name', 'done_at', 'created_at']


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ['id', 'items', 'title', 'created_at']

