import logging

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ForgotPasswordForm
from django.contrib.auth.models import User
from .models import Organisation, OrganisationUser, UserProfile
from django.contrib import messages
from django.conf import settings
import uuid
import ast
import os


def send_user_notification(user_details, user_token, template_id='63d94931-3b5a-42dc-ba0d-06b40902298b'):
    cloudfoundry_space = ast.literal_eval(settings.CLOUDFOUNDRY_SPACE).get('space_name', 'INVALID_SPACE') \
        if settings.CLOUDFOUNDRY_SPACE else 'localhost'
    if not settings.GOVUK_NOTIFY_DISABLE:
        if cloudfoundry_space in ['sandbox', 'staging']:
            account_verification_link = \
                f'https://cyberhealth-{cloudfoundry_space}.london.cloudapps.digital/account/account_verification/{user_token}'
        elif cloudfoundry_space == 'production':
            account_verification_link = \
                f'https://cyberhealth.london.cloudapps.digital/account/account_verification/{user_token}'
        else:
            account_verification_link = f'http://{cloudfoundry_space}:8000/account/account_verification/{user_token}'
        return settings.NOTIFICATIONS_CLIENT.send_email_notification(
            email_address=user_details.email,
            template_id=template_id,
            personalisation={
                'first_name': user_details.first_name,
                'account_verification': account_verification_link,
            }
        )
    else:
        dir_name = os.path.dirname(__file__)
        filename = os.path.join(dir_name, '../Spooler/url.txt')
        with open(filename, 'w') as file:
            file.write(f'http://{cloudfoundry_space}:8000/account/account_verification/{user_token}')


def get_message_status(notification_id):
    message_status = ''
    while message_status.lower() != 'delivered':
        message_status = settings.NOTIFICATIONS_CLIENT.get_notification_by_id(
            notification_id).get('status')
    return message_status


def deactivate_user(user_details):
    deactivated_user = User.objects.get(username=user_details.username)
    deactivated_user.is_active = False
    deactivated_user.save()


def activate_user(user_details):
    activated_user = User.objects.get(username=user_details.username)
    activated_user.is_active = True
    activated_user.save()


def account_activation(request, auth_token):
    try:
        user_profile_details = UserProfile.objects.filter(
            auth_token=auth_token).first()
        if user_profile_details:
            if user_profile_details.is_verified:
                messages.success(request, 'This account is already verified.')
                return redirect('login')
            activate_user(user_profile_details.user)
            user_profile_details.is_verified = True
            user_profile_details.save()
            return redirect('success-page')
        else:
            messages.error(request, 'The requested profile does not exist.')
            return redirect('create-an-account')
    except Exception as e:
        print(e)
        return render(request, error_page(request))


def error_page(request):
    return render(request, 'users/error_page.html')


def success_page(request):
    return render(request, 'users/success.html')


def send_token_page(request):
    user_info = User.objects.get(id=request.session['user'])
    return render(request, 'users/send_token.html', {'user_info': user_info})


def forgotten_password_page(request):
    logging.warning("forgotten_password_page: here")
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            redirect_url = reverse('password_reset_done')
            request.session['forgotten_password_email'] = request.POST['email']
            return HttpResponseRedirect(redirect_url)
    else:
        form = ForgotPasswordForm()
    return render(request, 'users/password_reset.html', {'form': form})


def forgotten_password_confirm_email(request):
    if 'forgotten_password_email' in request.session:
        email = request.session['forgotten_password_email']
    else:
        email = "not known"
    return render(request, 'users/password_reset_token.html', {'email': email})


def user_registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                organisation = Organisation.objects.get(
                    domain_name=form.cleaned_data.get('email').split('@')[-1])
                organisation_user = OrganisationUser.objects.filter(
                    user_organisation=organisation).first()
                if organisation_user is None and organisation:
                    user_info = form.save(commit=False)
                    auth_token = str(uuid.uuid4())
                    send_user_notification(user_info, auth_token)
                    user_info.username = user_info.email
                    user_info.save()
                    request.session['user'] = user_info.id
                    deactivate_user(user_info)
                    organisation.organisation_users_info.add(user_info)
                    user_profile = UserProfile.objects.create(
                        user=user_info, auth_token=auth_token)
                    user_profile.save()
                    redirect_url = reverse('send-token-page')
                    return HttpResponseRedirect(redirect_url)
                else:
                    messages.info(request, 'There is already a user for '
                                           'your local council.')
            except Exception as e:
                print(e)
                messages.error(request, 'There was an error in the sign up'
                                        ' process. Please check the details '
                                        'provided e.g. the email address. '
                                        'Please try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/create-an-account.html', {'form': form})
