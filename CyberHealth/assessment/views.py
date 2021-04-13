from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from assessment.models import Question

# Create your views here.

def index(request):

  return render(request, 'assessment/index.html')


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question' : question
    }


    return render(request, 'assessment/question.html', context)