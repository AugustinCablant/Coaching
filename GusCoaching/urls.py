"""GusCoaching URL Configuration
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    # Other URL patterns can go here
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.home, name='home'),

    # Password reset view
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    # Password reset done view
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # Password reset confirm view
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Password reset complete view
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),\
    
    path('dashboard/', views.dashboard, name='dashboard'),
]
