from django.urls import path

from . import views

urlpatterns = [
    path("product_form", views.product_form, name="product_form"),
    path('remove/<int:id>/', views.remove_product, name="remove_product"),
    path("product_list", views.product_list, name="product_list"),
    # path('get_modules/', views.get_modules, name='get_modules'),
    # path('get_sub_modules/', views.get_sub_modules, name='get_sub_modules'),
    # path("product_edit/<int:id>", views.product_edit, name="prdouct_edit"),
    
]

