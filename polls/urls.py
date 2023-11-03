from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.urls import path
from . import views 
from .forms import LoginForm

app_name = 'polls'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name= 'polls/login.html',authentication_form=LoginForm), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
