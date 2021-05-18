from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def start_page(request):
    return render(request, 'staticpages/index.html')

def privacy_policy(request):
    return render(request, 'staticpages/privacy-policy.html')

def cookie_policy(request):
    return render(request, 'staticpages/cookie-policy.html')

def accessibility_statement(request):
    return render(request, 'staticpages/accessibility-statement.html')
