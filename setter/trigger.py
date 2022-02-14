from django.shortcuts import redirect
from django.urls import reverse

from .models import Question

def delete_question(request, pk):

    question = Question.objects.get(id=pk)
    assignment = question.assignment
    question.delete()

    return redirect(reverse("setter:assignment-id", args=[assignment.id]))
