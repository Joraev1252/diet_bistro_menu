from django.urls import path

from .views import *

app_name = 'menu'

urlpatterns = [
    path('menu', meal_view, name='meal_view'),
    # path('', counterView, name='counter'),

]