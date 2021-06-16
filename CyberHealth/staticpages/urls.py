from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_page, name='static-page'),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('cookie-policy/', views.cookie_policy, name="cookie-policy"),
    path('accessibility-statement/', views.accessibility_statement, name="accessibility-statement"),
	path('pdf-tests/', views.pdf_tests),
    path('pdf-tests/privacy_view/', views.ViewPrivacyPDF.as_view(), name="pdf_view_privacy"),
    path('pdf-tests/privacy_download/', views.DownloadPrivacyPDF.as_view(), name="pdf_download_privacy"),
    path('pdf-tests/psn/', views.ViewPSNPDF.as_view(), name="pdf_view_psn"),
    path('pdf-tests/new/', views.render_pdf_view, name="test-view"),
    path('pdf-tests/weasy/', views.export_weasy_pdf, name="export_weasy"),
]
