from django.urls import path

from . import views

urlpatterns = [
    path("module_form/", views.module_form, name="module_form"),
    path("remove/<int:warehouse_id>/", views.remove_module, name="remove_module"),
    path("module_list/", views.module_list, name="module_list"),
    path("module_edit/<int:warehouse_id>", views.module_edit, name="module_edit"),
    
]

