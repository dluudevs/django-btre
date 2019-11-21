from django.contrib import admin

# in the same directory, import Listing. which is the name of the class in models
from .models import Listing

# extemds admin.ModelAdmin
class ListingAdmin(admin.ModelAdmin):
    # creates additional columns in admin area of listings
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    # makes the arguments clickable as links
    list_display_links = ('id', 'title')
    # create filter - common is required as python expects a list / tuple. this is true for all the items here
    list_filter = ('realtor',)
    # creates checkmark, allowing to toggle listing between published and unpublished in admin panel
    list_editable = ('is_published',)
    # Searchable by the fields passed in
    search_fields = ('title', 'description', 'address',  'city', 'state', 'zipcode', 'price')
    list_per_page = 25

# adds the model to django admin (localhost/admin)
admin.site.register(Listing, ListingAdmin)