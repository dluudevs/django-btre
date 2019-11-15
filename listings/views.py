from django.shortcuts import render

def index(request):
    # render will look inside the templates folder, this is possible from adding the template path in BTRE's settings.py
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

