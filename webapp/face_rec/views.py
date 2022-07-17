from django.shortcuts import render
from django.http.response import StreamingHttpResponse



def index(request):
    return render(request, 'face_rec/home.html')




