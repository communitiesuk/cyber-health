from django.shortcuts import render

# Create your views here.

def assessment_start_page(request):
  return render(request, 'assessment/index.html')
