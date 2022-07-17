from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def attendance(request):
    return render(request, 'dashboard.html', {'title': 'Dashboard'})
