from django.http import HttpResponse
from django.shortcuts import redirect, render
from face_rec.camera import *


def index(request):
    return render(request, 'face_rec.html')
