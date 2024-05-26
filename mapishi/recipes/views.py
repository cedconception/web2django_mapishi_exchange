import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group 

from .forms import RecipeForm, CommentAddForm

from .models import Recipe, Comment



def home(request):
    list_recipes = Recipe.objects.all()

    data = {
        'recipes': list_recipes 
    }

    return render(request, 'recipes/home.html', data)

def recipe_view(request, recipe_id):
    recipe = get_object_or_404( Recipe, id=recipe_id)
    comments = Comment.objects.filter(post=recipe).order_by('-time')

    if request.method == 'POST':
        comment_form = CommentAddForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = recipe
            comment.user = request.user
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        comment_form = CommentAddForm()
    
    data = {
        'recipe': recipe,
        'comments': comments,
        'form': comment_form,

    }
    return render(request, 'recipes/recipe_detail.html', data)

@login_required
@permission_required('recipes.add_recipe', raise_exception=True)
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipes:home') # ici on rentre à l'accueil
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
@permission_required('recipes.edit_custom_recipe', raise_exception=True)
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author and not is_administrator(request.user):
        raise PermissionDenied()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        
        if form.is_valid():
            if 'image' not in request.FILES:
                # Ne pas remplacer l'image existante si aucune nouvelle image n'est téléchargée
                form.cleaned_data['image'] = recipe.image
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

@login_required
def comment_add(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = recipe
            comment.user = request.user
            comment.save()
    
    return redirect('recipes:recipe_view', recipe_id=recipe_id)

def is_administrator(user):
    administrator = Group.objects.get(name='administrator')
    return user.groups.contains(administrator)


def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Recipe.objects.filter(title__icontains=query)
    else:
        results = Recipe.objects.none()
    return render(request, 'recipes/search_results.html', {'recipes': results, 'query': query})


