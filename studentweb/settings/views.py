from django.shortcuts import render
from django.http import HttpResponse

# Create your views here - SETTINGS views

def settingsHTML(request):
    return render(request, "settings.html")

