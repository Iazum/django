from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='about'),
        path('signin/', views.login, name='login'),
        path('signup/', views.logout, name='logout'),
        path('register/', views.register, name='register'),
        path('about/', views.about, name='about'),
        path('profile/', views.profile, name='profile')
        ]
