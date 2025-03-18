from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views         # google login

app_name = 'wellsip'

urlpatterns = [
    path('login/', views.login_screen, name='login-screen'),
    path('register/', views.register_screen, name='register-screen'),
    path('registration-data-submit/', views.store_registration_data, name='registration-data-submit'),
    path('resend-otp/', views.resend_otp, name='resend-otp'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('test/', views.test, name='test'),

    path('', views.home_screen, name='home'),
]