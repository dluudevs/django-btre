from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')), #first argument is the first segment of the URL for pages app. empty for home page to render upon load and /about for about page
    #second argument links to pages app's url.py file
    path('listings/',include('listings.urls')),
    # anything that has 'listings' in the url will be routed to the listings.url page
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is required to setup the media folder