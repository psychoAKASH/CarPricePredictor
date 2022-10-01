from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("predict/", views.predict, name="predict"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="Contact Us"),


]