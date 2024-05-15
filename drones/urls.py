from django.urls import path
from . import views


urlpatterns = [
    path('drones/', views.DroneListCreateView.as_view(), name='drones_list_create'),
    path('drones/<int:pk>/', views.DroneDetailView.as_view(), name='drone_detail'),
    path('drones/update/<int:pk>/', views.DroneUpdateView.as_view(), name='drone_update'),
    path('drones/delete/<int:pk>/', views.DroneDeleteView.as_view(), name='drone_delete'),
    path('drones/all/', views.DroneAllView.as_view(), name='drones_all'),
    path('drones/rent/<int:pk>/', views.RentalDroneView.as_view(), name='rent_drone'),
    path('rent/', views.AllRentalDroneView.as_view(), name='rent_drone'),
    path('', views.iha_list, name='ihalar'),
    path('create-iha/', views.drone_create_or_update_view, name='create_iha'),
    path('update-iha/<int:pk>/', views.drone_create_or_update_view, name='update_iha'),
    path('delete-iha/<int:pk>/', views.drone_delete_view, name='delete_iha'),

]