from django.contrib import admin
from django.urls import path

from recipes import views as recipes_views

#app_name = 'recipes'

urlpatterns = [
    # Home Page: Shows a list of recent articles
    path('', recipes_views.home, name='home'),
    path('recipes', recipes_views.home, name='home'),
    path('about', recipes_views.about, name='about_mapishi'),

    path('recipes/home/', recipes_views.home, name='home'),
    path('recipes/<int:recipe_id>', recipes_views.recipe_view, name='recipe_view'),
    #path('recipes/create', recipes_views.create_recipe, name='recipe'),

    
]