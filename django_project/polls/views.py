from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("설문조사 앱")
