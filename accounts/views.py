from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: login user and change redirect
            return HttpResponseRedirect('/accounts/login/')

    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
