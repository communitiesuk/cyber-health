from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from assessment.models import Question
from .forms import QuestionForm


def index(request):

    return render(request, 'assessment/index.html')


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm(question=question, choices=choices)

    context = {
        'question': question,
        'form': form,
    }

    return render(request, 'assessment/question.html', context)
