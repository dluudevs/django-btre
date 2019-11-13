from django.urls import path # required to use path
from . import views # . current directory

urlpatterns = [
    path('', views.index, name="index"),
    #root path (home page), is attached to views.index method, name is used to easily access this path
    #index method is created in views.py folder and renders for this url
    path('about', views.about, name="about") 
    # will render when path is /about
]