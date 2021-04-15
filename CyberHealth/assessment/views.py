from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from assessment.models import Question, Answer, Choice
from .forms import AnswerForm



def index(request):

    return render(request, 'assessment/index.html')


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(question=question)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        choice = get_object_or_404(Choice, pk=request.POST['choice'])
        answer = Answer(question=question, choice=choice)
        answer.save()
        return redirect('/assessment/') 

    context = {
        'form': form,
    }

    return render(request, 'assessment/question.html', context)
