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
    path('rename_assignment/<int:pk>', views.rename_assignment, name='rename-assignment'),
    path('delete_assignment/<int:pk>', views.soft_delete_assignment, name='delete-assignment'),
    path('restore_last_deleted_assignment/', views.restore_assignment, name='restore-assignment'),

    # Question add, edit and delete pages
    path('add_question/<int:pk>', views.add_question, name='add-question'),
    path('edit_question/<int:pk>', views.edit_question, name='edit-question'),
    path('delete_question/<int:pk>', views.delete_question, name='delete-question'),

]
