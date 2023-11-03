from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

