from django.shortcuts import render, redirect, get_object_or_404

from .form import VehicleForm, CategoryForm
from .models import Vehicle


# Create your views here.
def get_list_vehicle(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'list_vehicle.html', {"vehicles": vehicles})


def create_new_vehicle(request):
    vehicle_form = VehicleForm(request.POST or None)
    if vehicle_form.is_valid():
        vehicle_form.save()
        vehicle_form = VehicleForm()
        return redirect('/vehicle/')
    else:
        print(vehicle_form.errors)
    return render(request, 'create.html', {"form": vehicle_form})


def vehicle_detail(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'detail.html', {"vehicle": vehicle})


def vehicle_delete(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('/vehicle/')
    context = {
        "vehicle": vehicle
    }
    return render(request, "delete.html", context)


def vehicle_update(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if request.method == 'POST':
        form.save()
        return redirect('/vehicle/')
    context = {
        'form': form
    }
    return render(request, 'update.html', context)


def search_vehicle(request):
    # if request.method == 'POST':
    option = request.POST.get('option')
    keyword = request.POST.get('keyword')
    queryset = Vehicle.objects.all()
    if keyword and option:
        if option == 'select_here':
            raise Exception("Please pick option!")
        elif option == 'name':
            queryset = Vehicle.objects.filter(name__icontains=keyword)
        elif option == 'year':
            queryset = Vehicle.objects.filter(year__exact=keyword)
        elif option == 'transmission':
            queryset = Vehicle.objects.filter(transmission__icontains=keyword)
        elif option == 'category':
            queryset = Vehicle.objects.filter(category__name__contains=keyword)
        context = {
            "keyword": keyword,
            "vehicles": queryset.order_by('id')
        }
        return render(request, "list_vehicle.html", context)
    else:
        return redirect('/vehicle')


def create_new_category(request):
    category_form = CategoryForm(request.POST or None)
    if category_form.is_valid():
        category_form.save()
        category_form = CategoryForm()
        return redirect('/vehicle/')
    else:
        print(category_form.errors)
    return render(request, 'create_category.html', {"form": category_form})
