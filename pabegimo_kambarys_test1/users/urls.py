from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employees_register/', views.employees_register, name='employees_register')
]