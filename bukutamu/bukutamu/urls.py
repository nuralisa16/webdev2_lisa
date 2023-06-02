from django.contrib import admin
from django.urls import path

# from django.http import HttpResponse

# def buku_baru(req):
#     return HttpResponse('Teknik Informatika')

from django.shortcuts import render

def buku(req):
    return render(req, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', buku), 
]