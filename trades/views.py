from django.shortcuts import render
from django.http import HttpResponse

from .models import Trade


def index(req):
    trades = Trade.objects.all()
    return render(req, 'trades/index.html', {'trades': trades})
