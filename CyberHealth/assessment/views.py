from django.shortcuts import render
from assessment.models import Question

# Create your views here.

def index(request):
  return render(request, 'assessment/index.html')
