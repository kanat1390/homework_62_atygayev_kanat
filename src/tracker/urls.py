from django.urls import path
from tracker.views import (
    ProjectListView,
    ProjectDetailView,
    TaskDetailView,
    ProjectCreateView,
    TaskCreateView,
    TaskListView,
    ProjectUpdateView,
    TaskUpdateView,
    TaskDeleteView,
    ProjectDeleteView,
    ProjectParticipantsUpdateView
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/participants/update/', ProjectParticipantsUpdateView.as_view(), name="update_participants"),
]
