from django.shortcuts import render
from basicauth.decorators import basic_auth_required


@basic_auth_required
def start_page(request):
    return render(request, 'staticpages/index.html')
