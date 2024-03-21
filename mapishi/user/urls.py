from django.contrib import admin
from django.urls import path

from user import views as user_views

app_name = 'recipes'

urlpatterns = [
    # Home Page: Shows a list of recent articles
    #path('', user_views.home),
    path('community/', user_views.community),
]