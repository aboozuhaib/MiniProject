from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from . import 
# Display the 2 videos


def index(request):
    return render(request, 'face_rec/home.html')

# Every time you call the phone and laptop camera method gets frame
# More info found in camera.py


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Method for laptop camera


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 # video type
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# #Method for phone camera
# def webcam_feed(request):
# 	return StreamingHttpResponse(gen(IPWebCam()),
#                     #video type
# 					content_type='multipart/x-mixed-replace; boundary=frame')
