from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Rental
from .serializers import RentalSerializer
from .forms import RentalForm
from drones.models import Drone
from .models import Rental
from django.contrib.auth.models import User


# Create your views here.


class RentalDroneView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Rental.objects.filter(rental__user=self.request.user)
    
class AllRentalDroneView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        return Rental.objects.filter(rental__user=self.request.user)
    

class AddRentView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Rental.objects.filter(rental__user=self.request.user)
    

class AllRentView(generics.ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        return Rental.objects.filter(rental__user=self.request.user)
    

def rental_list(request):
    rentals = Rental.objects.filter(is_deleted=False)
    return render(request, 'rental_list.html', {'rental_list': rentals})  
    


def rental_create_or_update_view(request, pk=None):
    # get list user

    users = User.objects.all()



    if pk:
        rental = get_object_or_404(Rental, pk=pk)
    else:
        rental= None

    if request.method == 'POST':
        print(request.POST)
        form = RentalForm(request.POST, instance=rental)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(rental_list)
    else:
        form = RentalForm(instance=rental)                
    
    return render(request, 'rental_form.html', {'form': form, 'drones': Drone.objects.filter(is_deleted=False),'users': users})


def rental_delete_view(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    rental.is_deleted = True
    rental.save()
    return redirect(rental_list)
