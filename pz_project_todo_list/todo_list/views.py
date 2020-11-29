from pz_project_todo_list.todo_list.models import TodoList, TodoItem
from pz_project_todo_list.todo_list.serializers import TodoListSerializer, TodoItemSerializer, TodoItemUpdateSerializer
from rest_framework import generics, mixins


class TodoListList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoItemList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


class TodoItemDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.serializer_class = TodoItemUpdateSerializer
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
