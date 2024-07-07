from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/ids/', views.todos_ids, name='todos-ids'),
    path('todos/ids_titles/', views.todos_ids_titles, name='todos-ids-titles'),
    path('todos/unresolved/', views.todos_unresolved, name='todos-unresolved'),
    path('todos/resolved/', views.todos_resolved, name='todos-resolved'),
    path('todos/ids_userids/', views.todos_ids_userids, name='todos-ids-userids'),
    path('todos/resolved_userids/', views.todos_resolved_userids, name='todos-resolved-userids'),
    path('todos/unresolved_userids/', views.todos_unresolved_userids, name='todos-unresolved-userids'),
]
