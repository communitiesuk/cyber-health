from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserProfileForm


def user_registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('static-page')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})
