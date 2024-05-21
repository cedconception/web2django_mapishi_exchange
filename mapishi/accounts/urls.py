from accounts import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('profile/change/', views.change_profile, name='change_profile'),

    path('create/', views.create_account, name='create'),

]
