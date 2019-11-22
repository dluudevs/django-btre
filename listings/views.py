from django.shortcuts import render

# import model data and pass to html file
from .models import Listing

def index(request):

    listings = Listing.objects.all()

    # variable holds data from database, passed as an object to render in listings.html below (similar to MVC like React passing props)
    # inside listings.html, a for loop is used to dynamically generate markup for each listing
    context = {
        'listings': listings
    }

    # render will look inside the templates folder, this is possible from adding the template path in BTRE's settings.py
    return render(request, 'listings/listings.html', context)

# listing_id paramter passed in listing urls.py, must be passed here as well
def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

