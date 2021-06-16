import os
from django.shortcuts import render
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.views import View
from assessment.models import Control
from django.conf import settings
from weasyprint import HTML
import tempfile
from django.db.models import Sum


def export_weasy_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename="report.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string(
        'weasy.html', {'expenses':[],'total': 0})
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def render_pdf_view(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class ViewPrivacyPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('staticpages/privacy-policy.html')
		return HttpResponse(pdf, content_type='application/pdf')




class DownloadPrivacyPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('staticpages/privacy-policy.html')

		response = HttpResponse(pdf, content_type='application/pdf')
		content = "attachment; filename=Privacy_test.pdf"
		response['Content-Disposition'] = content
		return response



class ViewPSNPDF(View):
    def get(self, request, *args, **kwargs):
        controls = Control.objects.all()
        # for control in controls:
        #     print(control.subcontrol_set.all() )
        pdf = render_to_pdf('pdf_template.html', {'controls': controls})
        return HttpResponse(pdf, content_type='application/pdf')


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