from django.http import HttpResponse
from django.utils.timezone import now
from datetime import datetime
from datetime import timedelta



def index(request):
    return HttpResponse("Hello, world. You're at the cars index.")

