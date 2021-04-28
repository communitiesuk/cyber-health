from django.urls import path
from . import views

urlpatterns = [
  path('', views.assessment_start_page, name="index"),
  path('question/<int:question_id>', views.question_view, name="question"),
]
