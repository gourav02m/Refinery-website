from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    # path("starter/", views.starter, name="starter"),
        
]