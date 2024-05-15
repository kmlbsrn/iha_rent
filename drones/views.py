from django.shortcuts import render, redirect, get_object_or_404
from .models import Drone
from .serializers import DroneSerializer
from rest_framework import generics
from rest_framework.response import Response
from .forms import ProductForm
# Create your views here.


class DroneListCreateView(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    partial = True


class DroneDeleteView(generics.DestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(print(f"{instance} has been deleted"))


class DroneDetailView(generics.RetrieveAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneAllView(generics.ListAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class RentalDroneView(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Drone.objects.filter(rental__user=self.request.user)


class AllRentalDroneView(generics.ListAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    def get_queryset(self):
        return Drone.objects.filter(rental__user=self.request.user)


def iha_list(request):

    # if user authenticated then show all drones
    # if not authenticated then show only not rented drones
    if request.user.is_authenticated:
        drones = Drone.objects.all()
    else:
        drones = Drone.objects.filter(rental__isnull=True)

    return render(request, 'iha_list.html', {'drones': drones})

def iha_form_add(request):
    return render(request, 'iha_form.html')


# def product_create_view(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             # Form verilerini al
#             brand = form.cleaned_data['brand']
#             model = form.cleaned_data['model']
#             weight = form.cleaned_data['weight']
#             category = form.cleaned_data['category']

#             # Veritabanına kaydet
#             drone = Drone(brand=brand, model=model, weight=weight, category=category)
#             drone.save()

#             return redirect(iha_list)  # Başka bir sayfaya yönlendir

#     else:
#         form = ProductForm()

#     return render(request, 'iha_form.html', {'form': form, 'mode': 'create_iha'})


# def product_update_view(request, pk):
#     drone = get_object_or_404(Drone, pk=pk)

#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=drone)
#         if form.is_valid():
#             form.save()

#             return redirect('iha_list')  # İstediğiniz yönlendirme URL'sini buraya yazın
#     else:
#         form = ProductForm(instance=drone)

#     return render(request, 'iha_form.html', {'form': form, 'mode': 'update_iha'})


def drone_create_or_update_view(request, pk=None):
    if pk:  # Eğer pk değeri varsa, güncelleme işlemi yapılıyor
        drone = get_object_or_404(Drone, pk=pk)
    else:   # Yoksa, yeni bir drone oluşturuluyor
        drone = None

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=drone)
        if form.is_valid():
            form.save()
            return redirect(iha_list)  # İstediğiniz yönlendirme URL'sini buraya yazın
    else:
        form = ProductForm(instance=drone)

    return render(request, 'iha_form.html', {'form': form, 'drone': drone})



def drone_delete_view(request, pk):
    drone = get_object_or_404(Drone, pk=pk)
    drone.is_deleted = True
    drone.save()
    return redirect(iha_list)  # İstediğiniz yönlendirme URL'sini buraya yazın