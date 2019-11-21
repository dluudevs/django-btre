from django.contrib import admin

# in the same directory, import Listing. which is the name of the class in models
from .models import Listing

# adds the model to django admin (localhost/admin)
admin.site.register(Listing)