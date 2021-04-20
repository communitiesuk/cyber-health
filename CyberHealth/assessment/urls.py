from django.urls import path
from . import views

urlpatterns = [
    path('', views.assessment_start_page, name="assessment_start_page"),
]
