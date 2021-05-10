from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def user_registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
