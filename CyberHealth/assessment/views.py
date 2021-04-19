from basicauth.decorators import basic_auth_required
from django.shortcuts import render


@basic_auth_required
def assessment_start_page(request):
    return render(request, 'assessment/index.html')
