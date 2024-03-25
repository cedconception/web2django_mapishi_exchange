from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe



def home(request):
    list_recipes = Recipe.objects.all()

    data = {
        'recipes': list_recipes 
    }

    return render(request, 'recipes/home.html', data)

def recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    
    data = {
        'recipe': recipe 
    }
    return render(request, 'recipes/recipe_detail.html', data)

def create_recipe(request):
    return render(request, 'recipes/recipe_detail.html')

def about(request):
    return render(request, 'recipes/about.html')

