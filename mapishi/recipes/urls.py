from django.contrib import admin
from django.urls import path

from recipes import views as recipes_views

app_name = 'recipes'

urlpatterns = [
    # Home Page: Shows a list of recent articles
    path('', recipes_views.home, name='home'),
    path('recipes', recipes_views.home, name='home'),
    path('recipes/home/', recipes_views.home, name='home'),
    path('recipes/recipe_detail/', recipes_views.recipe, name='recipe'),

    
]