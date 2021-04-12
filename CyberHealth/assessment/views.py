from django.shortcuts import render
from assessment.models import Question

# Create your views here.

def index(request):
  test_q = Question.objects.create(
      question_text="Are users who install software or other active code on the Council’s systems without permission subject to disciplinary action?"
  )
  return render(request, 'assessment/index.html', {'question': test_q})
