from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from pz_project_todo_list.todo_list import views

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('docs/', include_docs_urls(title='Todo list')),
    path('todo-lists/', views.TodoListList.as_view(), name='todo-lists-list'),
    path('todo-lists/<int:pk>/', views.TodoListDetail.as_view(), name='todo-lists-detail'),
    path('todo-items/', views.TodoItemList.as_view(), name='todo-items-list'),
    path('todo-items/<int:pk>/', views.TodoItemDetail.as_view(), name='todo-items-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
