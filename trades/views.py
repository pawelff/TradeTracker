from django.shortcuts import render
from django.http import HttpResponse

from .models import Trade


def index(request):
    username = request.user.get_username()
    trades = Trade.objects.all()
    context = {
        'trades': trades,
        'username': username,
    }
    return render(request, 'trades/index.html', context)
