from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'recipes/home.html')
def recipe(request):
    return render(request, 'recipes/recipe_detail.html')
