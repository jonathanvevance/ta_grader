from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Assignment, Question
from .forms import QuestionForm


def dashboard(request):
    context = {
        'title': "Dashboard",
        'nbar_link': "dashboard",
    }
    return render(request, "setter/dashboard.html", context)

def assignments(request, pk=None):
    """ Show all assignments is just a simpler version of show particular assignment.
    That is the only reason why pk and hence loading an assignment is optional."""

    if pk: # TODO: does key exist check
        assignment = Assignment.objects.get(id=pk)
        questions = assignment.question_set.all()
    else:
        assignment, questions = None, []

    all_assignments = Assignment.objects.all()

    context = {
        'title': "Assignments",
        'nbar_link': "assignments",
        'questions': questions,
        'all_assignments': all_assignments,
        'this_assignment': assignment,
    }
    return render(request, "setter/assignments.html", context)

def edit_question(request, pk):
    """pk here is a question id."""

    # TODO: does key exist check
    my_question = Question.objects.get(id=pk)
    assignment = my_question.assignment
    form = QuestionForm(instance=my_question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=my_question)
        if form.is_valid():
            form.save()
            return redirect(reverse("setter:assignment-id", args=[assignment.id]))

    context = {
        'title': 'Question',
        'navbar_link': None,
        'form': form,
    }
    return render(request, "setter/question.html", context)

def add_question(request, pk):
    """pk here is an assignment id and NOT a question id."""

    assignment = Assignment.objects.get(id=pk)
    form = QuestionForm(initial={"assignment": assignment})

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            assignment_id = request.POST.get('assignment')
            return redirect(reverse("setter:assignment-id", args=[assignment_id]))

    context = {
        'title': 'Question',
        'navbar_link': None,
        'form': form,
    }
    return render(request, "setter/question.html", context)

def delete_question(request, pk):

    question = Question.objects.get(id=pk)
    assignment = question.assignment
    question.delete()

    return redirect(reverse("setter:assignment-id", args=[assignment.id]))

def add_assignment(request):

    assignment_name = request.POST.get("assignment-name")
    assignment = Assignment(title=assignment_name)
    assignment.save()

    return redirect(reverse("setter:assignment-id", args=[assignment.id]))

def rename_assignment(request, pk):

    assignment = Assignment.objects.get(id=pk)
    assignment_name = request.POST.get("assignment-name")
    assignment.set_title(assignment_name)
    assignment.save()

    return redirect(reverse("setter:assignment-id", args=[assignment.id]))

def delete_assignment(request, pk):

    assignment = Assignment.objects.get(id=pk)
    assignment.delete()

    return redirect(reverse("setter:assignments"))
