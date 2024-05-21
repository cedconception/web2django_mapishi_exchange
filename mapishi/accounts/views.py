from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from accounts.forms import UserChangeForm

@login_required
def user_profile(request):
    return render(request, 'registration/profile.html')

def password_change(request):
    return render(request, 'registration/password_change_form.html')

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse("login"))
    else:
        form = UserCreationForm()
    return render(request, 'registration/create_account.html', { 'form': form })

@login_required
def change_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile')
    else:
        form = UserChangeForm
    return render(request, 'registration/change_profile.html', { 'form': form })
