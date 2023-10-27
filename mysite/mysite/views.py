from django.http import HttpResponse
from django.utils.timezone import now
from datetime import datetime
from datetime import timedelta
from django.shortcuts import render


def index(request):
    dtt =datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    context = {
        'title': 'MAIN',
        'dtt': dtt,
    }
    return render(request, 'index.html', context=context)
