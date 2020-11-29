from pz_project_todo_list.todo_list.models import TodoList
from pz_project_todo_list.todo_list.serializers import SnippetSerializer
from rest_framework import generics


class TodoListList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = SnippetSerializer


class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = SnippetSerializer
