from django.shortcuts import render
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from assessment.models import Control


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

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