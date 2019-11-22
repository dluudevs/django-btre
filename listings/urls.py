from django.urls import path  # required to use path
from . import views  # . current directory

urlpatterns = [
    path('', views.index, name="listings"),
    # root path relates to "/listings" as setup in btre url
    path('<int:listing_id>', views.listing, name="listing"),
    # path will be /listings/id. a parameter is being created and passed to the view method
    path('search', views.search, name="search"),
    #  path will be listings/search but that is not necesssary here. in btre urls.py when the /about page is selected, the engine will look in this file for the urls
]
