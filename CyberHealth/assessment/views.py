from django.shortcuts import render
from basicauth.decorators import basic_auth_required


@basic_auth_required
def assessment_start_page(request):
    return render(request, 'assessment/index.html')
