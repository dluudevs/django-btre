from django.contrib import admin

# in the same directory, import realtorListing. which is the name of the class in models
from .models import Realtor

admin.site.register(Realtor)
