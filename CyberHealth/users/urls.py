from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('account_verification/<auth_token>/', views.account_activation, name='account-activation-page'),
    path('error/', views.error_page, name="error-page"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
