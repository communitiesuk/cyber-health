from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users.forms import LoginForm


urlpatterns = [
    path('account_verification/<auth_token>/', 
         views.account_activation, name='account-activation-page'),
    path('error/', views.error_page, name="error-page"),
    path('verify_account/', views.send_token_page, name="send-token-page"),
    path('account_activated/', views.success_page, name="success-page"),
    path('logout/', auth_views.LogoutView.as_view(
         template_name='users/logout.html'), name='logout'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
          template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done',
         auth_views.PasswordResetDoneView.as_view(
          template_name='users/send_token.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
          template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
          template_name='users/success.html'),
         name='password_reset_complete'),
    path('', auth_views.LoginView.as_view(
         template_name='users/login.html',
         authentication_form=LoginForm), name='login'),
]
