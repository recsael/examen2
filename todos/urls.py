from django.urls import path
from .views import (
    TodoListCreateAPIView, TodoDetailAPIView,
    todo_ids, todo_ids_titles, todo_unresolved,
    todo_resolved, todo_ids_userids,
    todo_resolved_userids, todo_unresolved_userids
)

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
    path('todos/ids/', todo_ids, name='todo-ids'),
    path('todos/ids_titles/', todo_ids_titles, name='todo-ids-titles'),
    path('todos/unresolved/', todo_unresolved, name='todo-unresolved'),
    path('todos/resolved/', todo_resolved, name='todo-resolved'),
    path('todos/ids_userids/', todo_ids_userids, name='todo-ids-userids'),
    path('todos/resolved_userids/', todo_resolved_userids, name='todo-resolved-userids'),
    path('todos/unresolved_userids/', todo_unresolved_userids, name='todo-unresolved-userids'),
]
