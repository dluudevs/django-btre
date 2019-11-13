from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')), #first argument is the first segment of the URL for pages app. empty for home page to render upon load and /about for about page
    #second argument links to pages app's url.py file
    path('admin/', admin.site.urls),
]
