from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/trades/')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
