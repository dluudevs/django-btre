from django.shortcuts import render

# import model data and pass to html file
from .models import Listing

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):

    # order by list date. hyphen is for descending order and filter to show only published items. is_published is a field in listings model.py
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # Paginator requires object for first argument, second argument is how many objects to display per page
    paginator = Paginator(listings, 6)
    
    # request object contains information about user's request
    # request.GET contains the get variables 
    # get returns the value for the given key, in this case, it returns the page index for the url parameter page. ie., what page number is this
    # get info on page (the url parameter we are looking for, ie ?page=1 in the url)
    page = request.GET.get('page')

    # get_page returns a page object (all the listings for that page based on the page index passed
    paged_listings = paginator.get_page(page)
    

    # variable holds data from database, passed as an object to render in listings.html below (similar to MVC like React passing props)
    # inside listings.html, a for loop is used to dynamically generate markup for each listing
    context = {
        'listings': paged_listings
    }

    # render will look inside the templates folder, this is possible from adding the template path in BTRE's settings.py
    return render(request, 'listings/listings.html', context)

# listing_id paramter passed in listing urls.py, must be passed here as well
def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

