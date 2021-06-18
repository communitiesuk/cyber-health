from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile


def render_to_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename="PSN_Code_of_Connection (CoCo).pdf"'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string(
        'psn-coco.html', {})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output = open(output.name, 'rb')
        response.write(output.read())

    return response

def start_page(request):
    return render(request, 'staticpages/index.html')

def privacy_policy(request):
    return render(request, 'staticpages/privacy-policy.html')

def cookie_policy(request):
    return render(request, 'staticpages/cookie-policy.html')

def accessibility_statement(request):
    return render(request, 'staticpages/accessibility-statement.html')

def pdf_tests(request):
	context = {}
	return render(request, 'pdf-tests.html', context)