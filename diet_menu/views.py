import psycopg2
from django.core.paginator import Paginator
from django.shortcuts import render
from hitcount.views import HitCountDetailView
import schedule
import time
from diet_menu.forms import VisitorsForm
from .models import MenuModel, CategoriesModel
from django.db.models import Q
from rest_framework.response import Response


def meal_view(request):

    meal = MenuModel.objects.all()
    first_meal = MenuModel.objects.filter(category_id=2)
    second_meal = MenuModel.objects.filter(category_id=3)
    garnirs = MenuModel.objects.filter(category_id=4)
    cotlets = MenuModel.objects.filter(category_id=5)
    bakery = MenuModel.objects.filter(category_id=6)
    salads = MenuModel.objects.filter(category_id=7)
    drinks = MenuModel.objects.filter(category_id=8)
    bread = MenuModel.objects.filter(category_id=9)

    title = CategoriesModel.objects.all()

    context = {
        "category": title,

        "meal": meal,
        "first_meal": first_meal,
        "second_meal": second_meal,
        "garnirs": garnirs,
        "cotlets": cotlets,
        "bakery": bakery,
        "salads": salads,
        "drinks": drinks,
        "bread": bread,
    }
    return render(request, 'menu.html', context)
