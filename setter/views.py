from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import Assignment, Question
from .forms import QuestionForm
from .tasks import schedule_hard_delete_assignment


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
            messages.success(request, "Edits made to the question have been saved")
            return redirect(reverse("setter:assignment-id", args=[assignment.id]))
        else:
            messages.error(request, "Errors need to be resolved")

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
            messages.success(request, "The question has been saved")
            return redirect(reverse("setter:assignment-id", args=[assignment_id]))
        else:
            messages.error(request, "Errors need to be resolved")

    context = {
        'title': 'Question',
        'navbar_link': None,
        'form': form,
    }
    return render(request, "setter/question.html", context)

def delete_question(request, pk):

    question = Question.objects.get(id=pk)
    question.delete()
    messages.success(request, "The question has been deleted")
    return redirect(request.META['HTTP_REFERER'])

def add_assignment(request):

    assignment_name = request.POST.get("assignment-name")
    assignment = Assignment(title=assignment_name)

    try:
        assignment.full_clean()
    except ValidationError as e:
        messages.error(request, Assignment.validation_error_message(e))
        return redirect(request.META['HTTP_REFERER'])

    assignment.save()
    messages.success(request, "The assignment has been added")

    return redirect(reverse("setter:assignment-id", args=[assignment.id]))

def rename_assignment(request, pk):

    assignment = Assignment.objects.get(id=pk)
    assignment_name = request.POST.get("assignment-name")
    assignment.set_title(assignment_name)

    try:
        assignment.full_clean()
    except ValidationError as e:
        messages.error(request, Assignment.validation_error_message(e))
        return redirect(request.META['HTTP_REFERER'])

    assignment.save()
    messages.success(request, "The assignment has been renamed")
    return redirect(request.META['HTTP_REFERER'])

def soft_delete_assignment(request, pk):

    assignment = Assignment.objects.get(id=pk)
    assignment.delete() # only soft deletion
    messages.success(request, "The assignment has been deleted")

    request.session['deleted_pk'] = pk
    messages.add_message(request, settings.UNDO_MSSG_LEVEL, "Click to Undo")
    schedule_hard_delete_assignment(pk) # scheduled hard deletion

    return redirect(reverse("setter:assignments"))

def restore_assignment(request):

    pk = request.session['deleted_pk']
    assignment = Assignment.all_objects.get(id=pk)
    assignment.restore()
    del request.session['deleted_pk']

    return redirect(reverse("setter:assignments"))
