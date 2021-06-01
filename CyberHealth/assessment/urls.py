from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessment_overview, name="assessment-overview"),
    path('test-upload', views.submit_evidence, name="test-upload"),
    path('<str:pathway_slug>/question/<int:question_id>', views.question_view, name="question"),
    path('all-questions',
         views.assessment_all_questions_page, name="all-questions"),
    path('<str:pathway_slug>', views.pathway_view, name="pathway"),
]
