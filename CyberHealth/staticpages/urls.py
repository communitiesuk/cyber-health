from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_page, name='static-page'),
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    path('cookie-policy', views.cookie_policy, name="cookie-policy"),
]
