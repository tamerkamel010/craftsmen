from django.urls import path 
import django.contrib.auth.views as auth_views
from . import views 


urlpatterns=[
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]