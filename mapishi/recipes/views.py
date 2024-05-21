import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required

from .forms import RecipeForm

from .models import Recipe



def home(request):
    list_recipes = Recipe.objects.all()

    data = {
        'recipes': list_recipes 
    }

    return render(request, 'recipes/home.html', data)

def recipe_view(request, recipe_id):
    recipe = get_object_or_404( Recipe, id=recipe_id)
    
    data = {
        'recipe': recipe 
    }
    return render(request, 'recipes/recipe_detail.html', data)

@login_required
@permission_required('recipes.add_custom_recipe', raise_exception=True)
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:home') # ici on rentre à l'accueil
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
@permission_required('recipes.edit_custom_recipe', raise_exception=True)
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_view', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
@permission_required('recipes.delete_custom_recipe', raise_exception=True)
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipes:home')
    return render(request, 'recipes/delete_recipe.html', { 'recipe': recipe })

@login_required
@permission_required('recipes.publish_recipe', raise_exception=True)
def publish_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        recipe.is_published = True
        recipe.date = datetime.time
        recipe.save()
        return redirect('recipes:recipe_view',  recipe_id=recipe.id)
    return render(request, 'recipes/delete_recipe.html', { 'recipe': recipe })


def about(request):
    return render(request, 'recipes/about.html')

