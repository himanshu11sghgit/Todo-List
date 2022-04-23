from django.urls import path 

from . import views


urlpatterns = [ 
    path('', views.TaskList.as_view(), name='task-list'),
    path('task_done/', views.TaskDoneList.as_view(), name='task-done-list'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('create/', views.TaskCreate.as_view(), name='task-create'),
    path('update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),
] 