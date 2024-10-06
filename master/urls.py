from django.urls import path

from . import views

urlpatterns = [

    path("master_form/", views.master_form, name="master_form"),
    path("remove/<int:plant_id>/", views.remove_master, name="remove_master"),
    path("master_list/", views.master_list, name="master_list"),
    path("master_edit/<int:plant_id>", views.master_edit, name="master_edit"),

]