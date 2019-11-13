from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    #render will look inside the templates folder, this is possible from adding the template path in BTRE's settings.py
    return render(request, 'pages/index.html') 

def about (request):
    return render(request, 'pages/about.html')