from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: login user and change redirect
            return HttpResponseRedirect('/accounts/login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
