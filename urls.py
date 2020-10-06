

from django.contrib import admin
from django.urls import path
from Home import views

admin.site.site_header = "Patel Idali Vada center Admin"
admin.site.site_title = "Patel Idali Vada center Admin Portal"
admin.site.index_title = "Welcome to Patel Idali Vada center Researcher Portal"

urlpatterns = [
    path("",views.index,name = 'Home'),
    path("About",views.about,name = 'About'),
    path("Services",views.services,name = 'Services'),
    path("Contact",views.contactInfo,name = 'Contact'),
]
