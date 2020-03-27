from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from .middleware import login_exempt
from django.contrib import messages

def employees(request):
    form = UserCreationForm()
    return render(request, 'users/employees.html', {'form': form})

def employees_register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Vartotojas sukurtas.')
        return redirect(reverse('users:employees'))
    else:
        return render(request, 'users/employees.html', {'form_errors': form.errors})