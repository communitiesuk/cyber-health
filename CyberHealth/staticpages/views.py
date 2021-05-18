from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def start_page(request):
    return render(request, 'staticpages/index.html')
