from django.db import models
from datetime import datetime
from realtors.models import Realtor
# read as, from realtors.models (app) import the Realtor model (class)

# Models are the source of information about an app's (in this case listing) data. Contains the essential fields and behavior of the data stored.
# Generally models map to a single database table
# Setting up a model in Python is easier and more organized than creating the database via SQL Shell or pgAdmin
# Documentation for fields: https://docs.djangoproject.com/en/2.2/ref/models/fields/


# Listing extends models.Model
class Listing(models.Model):
    # foreign key of another table (Realtor) to form a relationship between realtor and listings
    # second argument, do nothing when to the listing when the associated realtor is deleted
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    # the argument for TextField means this field is optional
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    # Photo is a string in the actual database, in Django there are different types of fields making it suitable for a image field
    # Argument defines where photos get uploaded to. Django has its own media folder, the argument will be the name of the folder inside of the media folder
    # it will look like this: <django media folder>/photos/YYMMDD
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    # below photos are optional
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    # In admin area, there will be a table that will display each listing. Below is the main field to be displayed

    def __str__(self):
        return self.title

# to move this to the database, in the terminal you must run the following commands
# python manage.py migrations
# this will create the migration files to tell the database what to do
# python manage.py migrate
# this will run the commands in the migratation files to create the tables in our database
        
        