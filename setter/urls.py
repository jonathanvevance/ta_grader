from django.urls import path

from . import views
from . import trigger

app_name = 'setter'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Assignments base and selected pages
    path('all_assignments/', views.assignments, name='assignments'),
    path('show_assignment/<int:pk>', views.assignments, name='assignment-id'),

    # Assignment add and delete pages
    path('add_assignment/', views.add_assignment, name='add-assignment'),
    path('delete_assignment/<int:pk>', views.delete_assignment, name='delete-assignment'),

    # Question add and edit pages
    path('add_question/<int:pk>', views.add_question, name='add-question'),
    path('edit_question/<int:pk>', views.edit_question, name='edit-question'),

    # Trigger functions - dummy pages
    path('trigger_delete_question/<int:pk>', trigger.delete_question, name='trigger-delete-question'),
]
