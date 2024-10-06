from django.urls import path

from . import views

urlpatterns = [
    
    path("submodule_form/", views.submodule_form, name="submodule_form"),
    path("remove/<int:section_id>/", views.remove_sub_module, name="remove_sub_module"),
    path("sub_module_list/", views.sub_module_list, name="sub_module_list"),
    path("sub_module_edit/<int:section_id>", views.sub_module_edit, name="sub_module_edit"),
    
]