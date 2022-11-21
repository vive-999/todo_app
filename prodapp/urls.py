from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update-todo'),
    path('reset_todo', views.reset_todo, name='reset-todo'),
    path('completed_todo', views.completed_todo, name='completed-todo'),
    path('pending_todo', views.pending_todo, name='pending-todo'),

]
