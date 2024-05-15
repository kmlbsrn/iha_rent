
from django.urls import path
from . import views


urlpatterns = [
    path('rentals/', views.rental_list, name='rental_list'),
    path('rentals/create/', views.rental_create_or_update_view, name='create_rental'),
    path('rentals/update/<int:pk>/', views.rental_create_or_update_view, name='update_rental'),
    path('rentals/delete/<int:pk>/', views.rental_delete_view, name='delete_rental'),

]