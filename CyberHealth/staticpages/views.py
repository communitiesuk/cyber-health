from django.shortcuts import render


def start_page(request):
    return render(request, 'staticpages/staticpage.html')
