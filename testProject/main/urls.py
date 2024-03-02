from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.lists, name="lists"),
    path("about", views.about, name="about"),
]
