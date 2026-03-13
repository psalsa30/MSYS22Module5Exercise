from django.shortcuts import render
from .models import Dish

# Create your views here.

def view_basic_list(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/basic_list.html', {'dishes':dish_objects})


def view_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/list.html', {'dishes':dish_objects})

def add_menu(request):
    return render(request, 'tapasapp/add_menu.html')

def view_wines(request):
    return render(request, 'tapasapp/view_wines.html')

def view_large_dishes(request):
    return render(request, 'tapasapp/view_large_dishes.html')

def view_coursed_menus(request):
    return render(request, 'tapasapp/view_coursed_menus.html')