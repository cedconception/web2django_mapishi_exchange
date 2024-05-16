from django.contrib import admin
from django.urls import path

from recipes import views as recipes_views

#app_name = 'recipes'

urlpatterns = [
    # Home Page: Shows a list of recent articles
    path('', recipes_views.home, name='home'),
    path('recipes', recipes_views.home, name='home'),
    path('about', recipes_views.about, name='about_mapishi'),

    path('recipes/home', recipes_views.home, name='home'),
    path('recipes/home/', recipes_views.home, name='home'),

    #recipe detailles
    path('recipes/<int:recipe_id>', recipes_views.recipe_view, name='recipe_view'),
    path('recipes/<int:recipe_id>/', recipes_views.recipe_view, name='recipe_view'),

    #ajouter
    path('recipes/add', recipes_views.add_recipe, name='add_recipe'),
    path('recipes/add/', recipes_views.add_recipe, name='add_recipe'),

    #edit
    path('recipes/<int:recipe_id>/edit', recipes_views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/edit/', recipes_views.edit_recipe, name='edit_recipe'),

    #effacer 
    path('recipes/<int:recipe_id>/delete', recipes_views.delete_recipe, name='delete_recipe'),
    path('recipes/<int:recipe_id>/delete/', recipes_views.delete_recipe, name='delete_recipe'),

    #la publication
    path('recipes/<int:recipe_id>/publish/', recipes_views.publish_recipe, name='publish_recipe'),

    
]