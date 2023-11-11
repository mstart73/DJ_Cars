from django.shortcuts import render
from datetime import datetime
# Create your views here.

def uppermenu(request):
    dtt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    context = {
        'title': 'MAIN',
        'dtt': dtt,
    }

    return render(request, 'uppermenu.html', context)