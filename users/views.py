from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid:
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})
