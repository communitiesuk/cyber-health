from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from assessment.models import Question

# Create your views here.

def index(request):
  test_q = Question.objects.create(
      question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
  )
  return render(request, 'assessment/index.html', {'question': test_q})


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question' : question
    }


    return render(request, 'assessment/question.html', context)