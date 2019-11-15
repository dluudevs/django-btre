from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), #first argument is the first segment of the URL for pages app. empty for home page to render upon load and /about for about page
    #second argument links to pages app's url.py file
    path('listings/',include('listings.urls')),
    # anything that has 'listings' in the url will be routed to the listings.url page
    path('admin/', admin.site.urls),
]