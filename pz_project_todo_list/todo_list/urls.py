from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from pz_project_todo_list.todo_list import views

urlpatterns = [
    path('todo-lists/', views.TodoListList.as_view()),
    path('todo-lists/<int:pk>/', views.TodoListDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)