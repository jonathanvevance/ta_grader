from django.urls import path

from . import views

app_name = 'setter'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Assignments base and selected pages
    path('all_assignments/', views.assignments, name='assignments'),
    path('show_assignment/<int:pk>', views.assignments, name='assignment-id'),

    # Assignment add, rename and delete pages
    path('add_assignment/', views.add_assignment, name='add-assignment'),
    path('delete_assignment/<int:pk>', views.delete_assignment, name='delete-assignment'),
    path('rename_assignment/<int:pk>', views.rename_assignment, name='rename-assignment'),

    # Question add, edit and delete pages
    path('add_question/<int:pk>', views.add_question, name='add-question'),
    path('edit_question/<int:pk>', views.edit_question, name='edit-question'),
    path('delete_question/<int:pk>', views.delete_question, name='delete-question'),

    # Trigger functions - dummy pages
]
