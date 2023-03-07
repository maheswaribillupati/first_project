from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rajesh(request):
    return HttpResponse("<h1>HE IS MY BEST FRIEND</h1>")
def mahendra(request):
    return HttpResponse("<marquee><h1>I LOVE MY BROTHER SO MUCH</h1></marquee>")